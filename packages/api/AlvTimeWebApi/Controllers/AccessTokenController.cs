using Microsoft.AspNetCore.Authorization;
using Microsoft.AspNetCore.Mvc;
using System.Collections.Generic;
using System.Linq;
using AlvTime.Business.DTOs;
using AlvTime.Business.Services;
using AlvTimeWebApi.ViewModels;
using AutoMapper;

namespace AlvTimeWebApi.Controllers
{
    [Route("api/user")]
    [ApiController]
    public class AccessTokenController : Controller
    {
        private readonly AccessTokenService _tokenService;
        private readonly IMapper _autoMapper;

        public AccessTokenController(AccessTokenService tokenService, IMapper autoMapper)
        {
            _tokenService = tokenService;
            _autoMapper = autoMapper;
        }

        [HttpPost("AccessToken")]
        [Authorize]
        public ActionResult<AccessTokenCreatedViewModel> CreateLifetimeToken([FromBody] AccessTokenRequestDto request)
        {
            var accessToken = _autoMapper.Map<AccessTokenCreatedViewModel>(_tokenService.CreateLifeTimeToken(request.FriendlyName));

            return Ok(accessToken);
        }

        [HttpDelete("AccessToken")]
        [Authorize]
        public ActionResult<IEnumerable<AccessTokenFriendlyNameViewModel>> DeleteAccessToken([FromBody] IEnumerable<AccessTokenDeleteDto> tokenIds)
        {
            var accessToken =
                _autoMapper.Map<List<AccessTokenFriendlyNameViewModel>>(
                    _tokenService.DeleteActiveTokens(tokenIds.Select(tokenIds => tokenIds.TokenId)));

            return Ok(accessToken);
        }

        [HttpGet("ActiveAccessTokens")]
        [Authorize]
        public ActionResult<IEnumerable<AccessTokenFriendlyNameViewModel>> FetchFriendlyNames()
        {
            var accessTokens = _autoMapper.Map<List<AccessTokenFriendlyNameViewModel>>(_tokenService.GetActiveTokens());

            return Ok(accessTokens);
        }
    }
}
