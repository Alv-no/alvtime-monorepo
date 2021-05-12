﻿using System.Collections.Generic;
using System.Globalization;
using System.Linq;

namespace AlvTime.Business.Holidays
{
    public class RedDaysService : IRedDaysService
    {
        public List<string> GetRedDays(int year, int fromYearInclusive, int toYearInclusive)
        {
            var dates = new List<string>();

            if (year != 0)
            {
                var redDays = new RedDays(year);

                foreach (var date in redDays.Dates)
                {
                    dates.Add(date.ToString("yyyy-MM-dd", CultureInfo.InvariantCulture));
                }
            }

            if (fromYearInclusive != 0 && toYearInclusive != 0)
            {
                var yearsToInclude = toYearInclusive - fromYearInclusive + 1;
                var years = Enumerable.Range(fromYearInclusive, yearsToInclude);

                foreach (var yearToFindDays in years)
                {
                    var redDays = new RedDays(yearToFindDays);

                    foreach (var date in redDays.Dates)
                    {
                        dates.Add(date.ToString("yyyy-MM-dd", CultureInfo.InvariantCulture));
                    }
                }
            }

            return dates;
        }
    }
}
