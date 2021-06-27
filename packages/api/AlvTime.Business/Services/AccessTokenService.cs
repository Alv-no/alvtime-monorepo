using System.Collections.Generic;
using AlvTime.Business.AccessToken;
using AccessTokenResponseDto = AlvTime.Business.DTOs.AccessTokenResponseDto;

namespace AlvTime.Business.Services
{
    public class AccessTokenService
    {
        private readonly IAccessTokenStorage _tokenStorage;

        public AccessTokenService(IAccessTokenStorage tokenStorage)
        {
            _tokenStorage = tokenStorage;
        }

        public AccessTokenResponseDto CreateLifeTimeToken(string friendlyName)
        {
            return _tokenStorage.CreateLifetimeToken(friendlyName);
        }

        public IEnumerable<AccessTokenResponseDto> DeleteActiveTokens(IEnumerable<int> tokenIds)
        {
            var response = new List<AccessTokenResponseDto>();

            foreach (var token in tokenIds)
            {
                response.Add(_tokenStorage.DeleteActiveTokens(token));
            }

            return response;
        }

        public IEnumerable<AccessTokenResponseDto> GetActiveTokens()
        {
            return _tokenStorage.GetActiveTokens();
        }
    }
}
