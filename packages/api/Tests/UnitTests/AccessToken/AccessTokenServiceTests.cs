using System.Collections.Generic;
using AlvTime.Persistence.Repositories;
using System.Linq;
using System.Security.Claims;
using AlvTime.Business.Services;
using AlvTime.Persistence.DataBaseModels;
using AlvTimeWebApi.AutoMapperProfiles;
using AlvTimeWebApi.Controllers.Utils;
using AutoMapper;
using Microsoft.AspNetCore.Http;
using Moq;
using Xunit;

namespace Tests.UnitTests.AccessToken
{
    public class AccessTokenServiceTests
    {
        [Fact]
        public void GetActiveAccessTokens_UserSpecified_ActiveTokensForUser()
        {
            var dbContext = new AlvTimeDbContextBuilder()
                .WithUsers()
                .CreateDbContext();

            var service = CreateAccessTokenService(dbContext);

            var tokens = service.GetActiveTokens();

            Assert.Equal(dbContext.AccessTokens.Where(x => x.UserId == 1).ToList().Count, tokens.Count());
        }

        [Fact]
        public void CreateLifetimeToken_FriendlyNameSpecified_TokenWithFriendlyNameCreated()
        {
            var dbContext = new AlvTimeDbContextBuilder()
                .WithPersonalAccessTokens()
                .WithUsers()
                .CreateDbContext();

            var service = CreateAccessTokenService(dbContext);

            service.CreateLifeTimeToken("new token");

            var tokens = service.GetActiveTokens();

            Assert.Equal(dbContext.AccessTokens.Where(x => x.UserId == 1).ToList().Count(), tokens.Count());
        }

        [Fact]
        public void DeleteToken_TokenIdSpecified_TokenWithIdDeleted()
        {
            var dbContext = new AlvTimeDbContextBuilder()
                .WithPersonalAccessTokens()
                .WithUsers()
                .CreateDbContext();

            var service = CreateAccessTokenService(dbContext);

            service.DeleteActiveTokens(new List<int>{1});

            var tokens = service.GetActiveTokens();

            Assert.Empty(tokens);
        }

        private static AccessTokenService CreateAccessTokenService(AlvTime_dbContext dbContext)
        {
            var mockHttpContextAccessor = GetHttpContextAccessor();

            var userContext = new UserContext(mockHttpContextAccessor.Object);

            var config = new MapperConfiguration(cfg => cfg.AddProfile<AccessTokenProfile>());
            var mapper = config.CreateMapper();

            return new AccessTokenService(new AccessTokenStorage(dbContext, userContext, mapper));
        }

        private static Mock<IHttpContextAccessor> GetHttpContextAccessor()
        {
            var httpContextAccessorMock = new Mock<IHttpContextAccessor>();
            httpContextAccessorMock.Setup(h => h.HttpContext.User).Returns(user);
            return httpContextAccessorMock;
        }

        private static ClaimsPrincipal user = new(
            new ClaimsIdentity(
                new[] { new Claim("preferred_username", "someone@alv.no") })
        );
    }
}
