# Appium BDD Example Framework

### Environment
- Common guide for Android SDK installation: [Link](https://github.com/testdevlab/TestRay/blob/master/SETUP.md#running-android-tests)
- Install [Node.js](https://nodejs.org/en)
- Install [Appium](https://github.com/appium/appium) by running `npm install -g appium`
- Install [Android Studio](https://developer.android.com/)
- Install [Oracle JDK 11](https://www.oracle.com/java/technologies/downloads/#java11) or [JDK 17](https://www.oracle.com/java/technologies/downloads/#java17)
    - As an alternative to Oracle JDK you can use [Temurin OpenJDK](https://adoptium.net/en-GB/temurin/releases/)
- Specify `ANDROID_HOME` and `ANDROID_SDK_ROOT` in your PATH [Link](https://developer.android.com/studio/command-line/variables)
- Specify `JAVA_HOME` in your PATH [Link for Mac](https://stackoverflow.com/questions/15826202/where-is-java-installed-on-mac-os-x)
- Install [Python 3.10+](https://www.python.org/downloads/)
- Add `venv` to the project [Link](https://docs.python.org/3/library/venv.html)
- Use Android device or emulator only.
- Optional: Install Allure using Homebrew to open the detailed report after test: `brew install allure`

### All Python packages installation
Simply run this command in the terminal:
```
python -m pip install -r requirements.txt
```

### Main Dependencies
- Appium-Python-Client: `python -m pip install git+https://github.com/testdevlab/Py-TestUI@bundle_id`
- Behave BDD: `python -m pip install behave`
- Allure-Behave: `python -m pip install allure-behave`

### Device setup
1. [For physical device] Open Settings on your Android device and scroll down to `About phone` option and tap on it 7 times. You will unlock the developer options with this action
2. [For physical device] Proceed to Developer options and enable `USB Debugging`
3. [For physical device] Attach your device to the computer via USB. It will likely show a prompt about trusting the computer, which you need to accept
4. Run `adb devices`, you will see a string of numbers and letters, followed by `device`. This string is your `udid`, you will need it pretty soon

### Capabilities
Appium uses [capabilities](https://appium.io/docs/en/latest/guides/caps/) to specify webdriver settings.
Most of the capabilities are specified under the hood in the `features/environment.py`, others you need to specify.
- UDID - specification of the execution device/emulator

### Almost ready
1. Make sure that you've set capabilities, your phone is attached with USB cable (or via tcp) and it is unlocked
2. In the projects root folder in the terminal type `adb install -r -t resources/app/fullAppForTestAutomation.apk`

### Start the test
In project's root directory type in terminal this command to run the test:
```
python -m behave features/login.feature
```

To start test and get the report after it type
```
python -m behave -f allure_behave.formatter:AllureFormatter -o ./features/artifacts/reports ./features
```

### After test
When the test would be finished, in the `features/artifacts` folder you can find screenshots for the successfully executed scenarios.

**If you have chosen an option with generating report:**
In the `features/artifacts/reports` folder, you can find an Allure report in JSON format.

If you want to open in the `html` format, just type
```
allure serve ./features/artifacts/reports
```

Note: Remember that `artifacts` folder (including screenshots and reports) would be cleared automatically when the next test run starts.

### Screenshot
![success](resourcesuccess_report.png)


### Contribute to this Example

If you want to contribute to this code example follow the next rules:

 1. Make sure the additions you are making doesnt break the existing test scenarios
 2. Make sure your new scenario or modifications work as intended
 3. Don't add scenarios that only covers the functionality already shown in other examples
 4. Before creating any new Scenario, create an issue in https://code.tdlbox.com/coe/ui-automation/python/pytestui-web-example/-/issues
 5. Before creating a merge request you must add a comment with the pylint score (pylint ./features -> 10/10)# pytestui-mob-example-M_zvinis
