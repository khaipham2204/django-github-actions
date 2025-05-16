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
            types: [opened]

- Webhook events
    name: Webhook Events
    on:
    issues:
        types: [opened]

# Jobs
jobs:
    name-of-workflow:
        runs-on: ubuntu-latest

# Steps
steps:
    - run: >
        echo "User ${{ github.event.inputs.username }} ran workflow manually."
        echo "Because ${{ github.event.inputs.reason }}."


# Actions
jobs:
    name-of-workflow:
        runs-on: ubuntu-latest
        steps:
        - uses: actions/stale@v3

# Runners
- GitHub-hosted runners
- Self-hosted runners