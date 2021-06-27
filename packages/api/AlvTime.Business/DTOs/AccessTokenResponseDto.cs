namespace AlvTime.Business.DTOs
{
    public record AccessTokenResponseDto (int Id, string Token, string ExpiryDate, string FriendlyName);
}
