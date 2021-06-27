using System;
using AlvTime.Business.DTOs;
using AlvTime.Business.Utils;
using AlvTime.Persistence.DataBaseModels;
using AlvTimeWebApi.AutoMapperProfiles;
using AutoMapper;
using Xunit;

namespace Tests.UnitTests.AutoMapper
{
    public class AccessTokenMappingTests
    {
        [Fact]
        public void AccessTokenToAccessTokenResponseDto_PropertiesShouldMatch()
        {
            var config = new MapperConfiguration(cfg => cfg.AddProfile<AccessTokenProfile>());
            var mapper = config.CreateMapper();

            var accessToken = new AccessTokens
            {
                Id = 1,
                UserId = 1,
                Value = Guid.NewGuid().ToString(),
                ExpiryDate = DateTime.UtcNow,
                FriendlyName = "My Token"
            };

            var mappedToken = mapper.Map<AccessTokenResponseDto>(accessToken);

            Assert.Equal(mappedToken.Token, accessToken.Value);
            Assert.Equal(mappedToken.ExpiryDate, accessToken.ExpiryDate.ToDateOnly());
            Assert.Equal(mappedToken.FriendlyName, accessToken.FriendlyName);
        }
    }
}
