# django-github-actions
The core components and concepts:
- Events
- Jobs
- Steps
- Actions
- Runners

# Events
- Scheduled events: cron syntax
    on:
        schedule:
            - cron: '*/5 * * * *' # triggered every 5 minutes.
- Manual events
    on:
        workflow_dispatch: # the workflow must be on the default branch.
            inputs:
                username:
                    description: "Your Github username"
                    required: true
                reason:
                    description: "Running this workflow"
                    required: true
                    default: "Running before testing."
        repository_dispatch:
- Webhook events