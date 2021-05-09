![Screenshot][./S1.jpeg]

![Screenshot][./S2.jpeg]

*Bots Rise!*

Get your copy of the chatbot:

    `$ git clone `

Sit back and relax. The chatbot offers a one step installation. Run : 

    `$ make setup`

*Note*: The above can fail in case of dependency issues on your local. If you wish to continue without upgrading to the following recommended requirements: 

- pip3 (version > 20)
- python3 (<= 3.7)
- Tensorflow tools (>=12)
- python3-dev (>1.17.0)
- Rasa (=2.6.0)

**Manual Steps** :

To fulfill minimum requirements, run the follwoing chain of commands which will test and upgrade all the packages needed to fire up your bot : 
    
    `$ pip3 install --upgrade pip`

    `$ python3 install --upgrade python`

    `$ python3 -m pip install python-dev-tools --user --upgrade`

Install Rasa :
    
    `pip3 install rasa`

Train your modules :
    
    `rasa train`

Run the following command in a new terminal to get the action server live : 

    `rasa run actions`

Your bot is now up and running! Open a third terminal and run the follwoing command to be able to talk to  your assistant :

    `rasa shell`


