# Logerator
Generaor of log files for testing purposes

## Idea
Original needs was about logfiles which will grow over the time with random messages in it and random timing in order to go trough testing. 

## How it work
First of all you need to change configuration in log_config.yaml here you can find following:

    start_time: "08:00" - time when logger should start working in the morning in case if it will work for more than one day
    end_time: "19:00" - time when logger should stop working in the morning in case if it will work for more than one day
    delays: 60 - this parameter used as limitation of random delay in seconds, means new line can appear any time in near 60 sec
    sample_file: "sample.log" - file with samples of log strings
    output_file: "businesapp.log" - output file for continious logging

then we need to provide some string templates from which we will select randomly a line and put it into output file. In order to do this we need to put such templates in sample file, normally in should be something around 65% Normal, 15% Warning, 10% Minor, 7% Major and 3% Critical lines. I believe it will be quite close to reality.

Then all that you need to do just run it. 

## Important
In some cases you can get an error message that yaml packcge not found, in this case please run following command:

pip install pyyaml
