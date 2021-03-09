#  WhosIt

A <em>Whosit</em> is a simple python script /application that is used to capture keystrokes and send it to a destination mail. The log file will include the <b>Key pressed, date and time.</b>The main modules/libraries used in this script are: schedule, pynput, and os. When the file is executed for the first time, a text file is created at a particular location(hidden), the key log information is sent every 30 mins to the target email(you can change the target and destination email).The regular py, pyw(no console) file and a exe is provided within the repository.

<h2>Working</h2>
The script first checks if a python script/exe exists in the start up directory of the victim's computer computer(currently logged in user).If not, then the script creates a copy of the python script/exe in the startup folder and also a text file in AppData directory(can be changed). After the creation, it will be made hidden.Each time the user, starts the computer the script also starts executing ,and will capture the keystrokes and sent it to the target email in an interval of 30 mins.

<h2>Requiremnents</h2>
<ul>
<li>Schedule</li>
<li>Pynput</li>
</ul>
<h2>Changes that you should make.</h2>
