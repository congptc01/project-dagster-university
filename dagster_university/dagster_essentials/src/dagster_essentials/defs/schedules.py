from dagster_essentials.defs.jobs import weekly_update_job

import dagster as dg

weekly_update_schedule = dg.ScheduleDefinition(
    job=weekly_update_job,
    cron_schedule="0 0 * * 1",  # every Monday at midnight
)
