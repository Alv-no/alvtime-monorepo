using AlvTimeWebApi.Dto;
using AlvTimeWebApi.HelperClasses;
using AlvTimeWebApi.Persistence.DatabaseModels;
using Microsoft.AspNetCore.Authorization;
using Microsoft.AspNetCore.Mvc;
using System;
using System.Collections.Generic;
using System.Globalization;
using System.Linq;

namespace AlvTimeWebApi.Controllers.TimeEntries
{
    [Route("api/user")]
    [ApiController]
    public class TimeEntriesController : Controller
    {
        private readonly AlvTime_dbContext _database;
        private ExistingObjectFinder checkExisting;

        public TimeEntriesController(AlvTime_dbContext database)
        {
            _database = database;
            checkExisting = new ExistingObjectFinder(_database);
        }

        [HttpGet("TimeEntries")]
        [Authorize]
        public ActionResult<IEnumerable<TimeEntriesResponseDto>> FetchTimeEntries(DateTime fromDateInclusive, DateTime toDateInclusive)
        {
            try
            {
                var user = RetrieveUser();

                var hours = _database.Hours
                    .Where(x => x.Date >= fromDateInclusive && x.Date <= toDateInclusive && x.User == user.Id)
                    .Select(x => new TimeEntriesResponseDto
                    {
                        Id = x.Id,
                        Value = x.Value,
                        Date = x.Date.ToString("yyyy-MM-dd", CultureInfo.InvariantCulture),
                        TaskId = x.TaskId
                    })
                    .ToList();

                return Ok(hours);
            }
            catch (Exception e)
            {
                return BadRequest(new
                {
                    Message = e.ToString(),
                });
            }
        }

        [HttpPost("TimeEntries")]
        [Authorize(Policy = "AllowPersonalAccessToken")]
        public ActionResult<List<TimeEntriesResponseDto>> UpsertTimeEntry([FromBody] List<CreateTimeEntryDto> requests)
        {
            List<TimeEntriesResponseDto> response = new List<TimeEntriesResponseDto>();
            var user = RetrieveUser();

            foreach (var request in requests)
            {
                try
                {
                    Hours timeEntry = checkExisting.RetrieveExistingTimeEntry(request, user);
                    if (timeEntry == null)
                    {
                        timeEntry = CreateNewTimeEntry(request, user);
                    }

                    var task = _database.Task
                        .Where(x => x.Id == timeEntry.TaskId)
                        .FirstOrDefault();

                    if (timeEntry.Locked == false && task.Locked == false)
                    {
                        timeEntry.Value = request.Value;
                        _database.SaveChanges();

                        var responseDto = new TimeEntriesResponseDto
                        {
                            Id = timeEntry.Id,
                            Date = timeEntry.Date.ToString("yyyy-MM-dd", CultureInfo.InvariantCulture),
                            Value = timeEntry.Value,
                            TaskId = timeEntry.TaskId
                        };

                        response.Add(responseDto);
                    }
                }
                catch (Exception e)
                {
                    return BadRequest(new
                    {
                        Message = e.ToString()
                    });
                }
            }
            return Ok(response);
        }

        private User RetrieveUser()
        {
            var username = User.Claims.FirstOrDefault(x => x.Type == "name").Value;
            var email = User.Claims.FirstOrDefault(x => x.Type == "preferred_username").Value;
            var alvUser = _database.User.FirstOrDefault(x => x.Email.Equals(email));

            return alvUser;
        }

        private Hours CreateNewTimeEntry(CreateTimeEntryDto hoursDto, User user)
        {
            Hours hour = new Hours
            {
                Date = hoursDto.Date.Date,
                TaskId = hoursDto.TaskId,
                User = user.Id,
                Year = (short)hoursDto.Date.Year,
                DayNumber = (short)hoursDto.Date.DayOfYear
            };
            _database.Hours.Add(hour);
            return hour;
        }
    }
}