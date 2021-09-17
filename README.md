# What is it?

The University of Guelph requires a Covid Self-Declaration form to be filled daily to permit access to Campus resources. Rather than take the chance of forgetting to complete this, I made a quick script to do so, which I intend on running on a slave VM on a daily CRON schedule.

## Assumptions

This program assumes the user has a compatible version of Firefox installed on their machine.

## How to configure

Currently, the program only supports the declaration of students and visitors, in which the config.json file should be filled in the following structure:

```json
{
    "student": [
        {
            "fullName": "John Smith",
            "email": "jsmith@email.com",
            "mobile": "1234567890"
        }
    ],
    "guest": [
        {
            "fullName": "Margaret Smith",
            "email": "msmith@email.com",
            "mobile": "0987654321"
        }
    ]
}
```

## How to use

You may prefer to create a virtual environment before installing the requirements, but I use selenium in a number of projects, so I have it installed globally. Regardless, type the following to install the required libraries.

`pip install -r requirements.txt`

This may require some configuration to add geckodriver to the executable path. More help can be found [here](https://softwaretestingboard.com/q2a/2366/how-to-set-geckodriver-into-path-environment-variable)

Once you have set up your environment, enter the following to run the program

`python3 run.py`

Voilà! You can also run this program on a CRON schedule like I am to completely forget about having to run this program.
