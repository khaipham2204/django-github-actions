name:
on:
    types: [my-event]
jobs:
    job_A:
    job_B:
        needs: jobA
    job_C:
        needs: [jobA, jobB]

    runs-on: ubuntu-latest
    steps:
    -  uses: actions/stale@v3
    -  run: >
        echo "User ${{ github.event.inputs.username }} ran a workflow manually."
        echo "Because ${{ github.event.inputs.reason }}."
