using System.Linq;
using AlvTime.Business.Interfaces;
using Microsoft.AspNetCore.Http;

namespace AlvTimeWebApi.Controllers.Utils
{
    public class UserContext : IUserContext
    {
        private readonly IHttpContextAccessor _httpContextAccessor;

        public UserContext(IHttpContextAccessor httpContextAccessor)
        {
            _httpContextAccessor = httpContextAccessor;
        }

        public string Name => _httpContextAccessor.HttpContext.User.Claims.FirstOrDefault(x => x.Type == "name").Value;
        public string Email => _httpContextAccessor.HttpContext.User.Claims.FirstOrDefault(x => x.Type == "preferred_username").Value;
    }
}
