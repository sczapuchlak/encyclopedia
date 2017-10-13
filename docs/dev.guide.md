# How to set your system up for development
## dependencies
> All commands will be listed for use in either PowerShell for Windows or Terminal for macOS

### Installing project dependencies can be done with the following command

`pip install -r requirements.txt`

This will install all of the items listed in the file `requirements.txt`

### Installing the tools to make development easier

1. first a requriement is that NodeJS is installed on your system, you can install
   this by visiting [their website](https://nodejs.org/en/). Either version available
   there should work just fine.
2. Once NodeJS is installed you now can freely use [npm](https://www.npmjs.com/) to 
   install javascript dependencies, you may need to restart your computer to get access
   to the following commands.
3. The command `npm i` will install all of the dependencies listed in the project.json
   file in our project directory. These dependencies will be placed in a new folder called
   node_modules

### Setting up the dev environment

We are using environment variables to store private information, the following env variables need to be set

* twitter_access_key
* twitter_access_secret
* twitter_consumer_key
* twitter_consumer_secret
* giphy_access_key

To set thses you need to run the following command

#### powershell
```powershell
$evn:variable = "secret_string"
```

#### terminal
```bash
export $varialbe='secret_string'
```

Replacing the variable and secret_string items with the valid variable name and key/secret

### Running the server

At this point you should be all set to run the application, the following command will run the server with browser sync automatically refreshing your browser when any changes are made.

`gulp`

> #### Note
>
> Because of the way nodejs/npm is setup differently on differnt computers, you may need to run `./node_modules/.bin/gulp`. 
>
>Alternatly tou can also set your path to include this folder, I recomend doing this only for your terminal session. You can do this by running one of the following:
>
> #### powershell
> ```powershell
> $env:path = "$env:path;./node_modules/.bin/"
> ```
>
> #### terminal
> ``` bash
> export $PATH=$PATH+';./node_modules/.bin/'
> ```

At this point a browser should have opened and navigated to the site running locally on your computer. The server is configured to automatically restart when changes are made to any of the .py files and browser sync will automatically refresh your browser when any .css, .js or .html file is saved.