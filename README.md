# azure_flask_deployment
This is assignment #2 for HHA504

## Setting up cloud shell for flask application
I decided to use Professor Hamts' flask applications that we worked on during class.
I used flaskapp_0.
I created a app.py file and copied the data from professors Hants' git repository to cloud shell file "app.py"
I also created a about.html file and copied the data from professor Hants' git repositrory to cloud shell file "about.html.
I also added a new variable to the base.html file where it takes a name and displays: "Hi this is Fahima!". The name variable value is "Fahima".

## Flask Application deployment
First I needed to connect my azure account to my cloud shell, so I used this [link](https://learn.microsoft.com/en-us/cli/azure/install-azure-cli-linux?pivots=apt) and I chose my school email which then gave me a code and a link on cloud shell. I clicked the link and put in the code to the website I was navigated to. 
In my cloud shell terminal I put in `az` (insuring I was in the right file: "azure_flask_deplyment")
Then procceded with `az login --use-device-code`
I used this code to get my subscription ID - `az account list --output table`
I copied the third subsription code and placed it after this code: `az account set --subscription (my subscription code here)`.
Then I went to the azure web page and typed in resource group in the serach bar and created a group name: Fahima-504
After, I added this code to my shell terminal: 
`az webapp up --resource-group <groupname> --name <app-name> --runtime <PYTHON:3.9> --sku <B1>` for group name I copied the resource group from azure which was `fahima.lakhi_rg_5035` and for the app name I copied from name under web app which was `fahima-504-flask` (this information was found in home - app services - fahima-504-flask)
When I tried `az webapp up` to re-deploy I was presented with an error that read "could not auto-detect the runtime stack of your app". 
I then added the run time flag  --runtime <PYTHON:3.9> to `az webapp up` this fixed the error 
once I deployed I realized that there was an application error. On azure I looked at the log streams I saw there was an error, the error was "no module named pandas." I relized this was because I misspelled requirenments.txt file (silly mistake). 
I re-deployed after fixing my mistake, by using `az webapp up --runtime <PYTHON:3.9>` 


# This is my deployed URL of my application : fahima-504-flask.azurewebsites.net