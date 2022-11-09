# Task 1: Software Configuration
### Subtask 1: Why did I choose to participate in the Dare IT Challenge?
Hello! My name is Iryna, and I set myself the goal of changing my profession. I love technology very much, and therefore I have always been interested in more and more complex processes that I can accomplish with its help.

I saw this Challenger on Instagram and immediately decided to register. I see it as an opportunity to gain new knowledge in testing, and my goal is to work in the IT field. A modern profession in a progressive field will help me to be in good shape all the time.

#### Sincerely,
#### Iryna.

# Task 2: Selectors
### **scouts_panel_xpath**
```
//h5[contains(text(),"Scouts")]
//h5[not(@id)]
//h5/.
```
### **login_xpath**
```
//*[@id='login']
//*[@name='login']
//div[1]/div/input
```
### **password_xpath**
```
//*[@id="password"]
//input[contains(@type,'password')]
//input[starts-with(@id,'p')]
```
### **remaind_password_xpath**
```
//a[@tabindex='-1']
//a[contains(text(),"Remind")]
//*[contains(@class,"jss37")]
```
### **language_select_xpath**
```
//*[@role='button']
//*[contains(@class,"Menu")]
//div[starts-with(@aria-haspopup,"l")]
```
### **sing_in_button_xpath**
```
//div[2]/button
//div/descendant::button
//*[@type="submit"]
```