using System.Collections.Generic;
using AlvTime.Business.DTOs;

namespace AlvTime.Business.AccessToken
{
    public interface IAccessTokenStorage
    {
        IEnumerable<AccessTokenResponseDto> GetActiveTokens();
        AccessTokenResponseDto DeleteActiveTokens(int tokenId);
        AccessTokenResponseDto CreateLifetimeToken(string friendlyName);
    }
}
