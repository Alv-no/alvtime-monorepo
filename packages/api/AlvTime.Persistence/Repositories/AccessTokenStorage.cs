using AlvTime.Business.AccessToken;
using AlvTime.Persistence.DataBaseModels;
using System;
using System.Collections.Generic;
using System.Linq;
using AlvTime.Business.DTOs;
using AlvTime.Business.Interfaces;
using AlvTime.Business.Utils;
using AutoMapper;
using User = AlvTime.Persistence.DataBaseModels.User;

namespace AlvTime.Persistence.Repositories
{
    public class AccessTokenStorage : IAccessTokenStorage
    {
        private readonly AlvTime_dbContext _dbContext;
        private readonly IUserContext _userContext;
        private readonly User _user;
        private readonly IMapper _autoMapper;

        public AccessTokenStorage(AlvTime_dbContext dbContext, IUserContext userContext, IMapper autoMapper)
        {
            _dbContext = dbContext;
            _userContext = userContext;
            _autoMapper = autoMapper;
            _user = _dbContext.User.First(user => user.Email.ToLower().Equals(_userContext.Email.ToLower()));
        }

        public AccessTokenResponseDto CreateLifetimeToken(string friendlyName)
        {
            var accessToken = new AccessTokens
            {
                UserId = _user.Id,
                Value = Guid.NewGuid().ToString(),
                ExpiryDate = DateTime.UtcNow.AddMonths(6),
                FriendlyName = friendlyName
            };

            _dbContext.AccessTokens.Add(accessToken);
            _dbContext.SaveChanges();

            return new AccessTokenResponseDto(accessToken.Id, accessToken.Value, accessToken.ExpiryDate.ToDateOnly(), accessToken.FriendlyName);
        }

        public AccessTokenResponseDto DeleteActiveTokens(int tokenId)
        {
            var token = _dbContext.AccessTokens
                .FirstOrDefault(t => t.Id == tokenId && t.UserId == _user.Id);

            token.ExpiryDate = DateTime.UtcNow;
            _dbContext.SaveChanges();

            return _autoMapper.Map<AccessTokenResponseDto>(token);
        }

        public IEnumerable<AccessTokenResponseDto> GetActiveTokens()
        {
            var tokens = _dbContext.AccessTokens
                .Where(token => token.UserId == _user.Id && token.ExpiryDate >= DateTime.UtcNow)
                .ToList();

            return _autoMapper.Map<List<AccessTokenResponseDto>>(tokens);
        }
    }
}
