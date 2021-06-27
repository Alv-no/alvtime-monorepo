using AlvTime.Business.DTOs;
using AlvTime.Business.Utils;
using AlvTime.Persistence.DataBaseModels;
using AlvTimeWebApi.ViewModels;
using AutoMapper;

namespace AlvTimeWebApi.AutoMapperProfiles
{
    public class AccessTokenProfile : Profile
    {
        public AccessTokenProfile()
        {
            CreateMap<AccessTokenResponseDto, AccessTokenCreatedViewModel>();
            CreateMap<AccessTokenResponseDto, AccessTokenFriendlyNameViewModel>();
            CreateMap<AccessTokens, AccessTokenResponseDto>()
                .ForMember(x => x.ExpiryDate,
                    opt => opt.MapFrom(src => src.ExpiryDate.ToDateOnly()))
                .ForMember(x => x.Token,
                opt => opt.MapFrom(src => src.Value))
                .ForCtorParam("Token", opt => opt.MapFrom(src => src.Value));
        }
    }
}
