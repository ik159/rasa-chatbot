#!/bin/bash

echo "Bots rise!"
echo "While we set up your bot, go ahead and deploy your action server. 1. Open another server tab and run `rasa run actions` 2. To be able to interact with your bot, open a third server tab and run `rasa shell`"
echo "Setting up your bot" | pip3 install rasa && rasa train