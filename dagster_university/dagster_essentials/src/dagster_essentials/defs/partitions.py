from dagster_essentials.defs.assets import constants

import dagster as dg

start_date = constants.START_DATE
end_date = constants.END_DATE

weekly_partition = dg.WeeklyPartitionsDefinition(
    start_date=start_date, end_date=end_date
)


monthly_partition = dg.MonthlyPartitionsDefinition(
    start_date=start_date, end_date=end_date
)
