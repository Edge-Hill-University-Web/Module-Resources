# 🔐 Web Teaching Environment – CSRF Token Error Guide

**Issue:**  
When attempting to log in, you may see the message:  
> **“The CSRF token is invalid. This might indicate a malicious attack.”**

This error occurs when your browser’s session cookies or cache interfere with the website’s security token used for form validation.

---

# 🧭 Steps to Fix the Error

## **Option 1**: Clear Cookies / History and Refresh Page



![Example of CSRF token error on login page](https://raw.githubusercontent.com/Edge-Hill-University-Web/Module-Resources/refs/heads/main/WTE_Clear_Refresh.gif "CSRF Token Error Example")  
*Example of the login error as shown on the Web Teaching Environment page.*


### 1. Clear Cookies and Cache  
1. Open your browser’s **Settings**.  
2. Go to **Privacy and Security → Clear Browsing Data**.  
3. This will remove **cookies** and **cached files** for the domain `edgehill.ac.uk`.  

### 2. Refresh the Page  
Next, refresh (`Ctrl + R` or `⌘ + R`) reloads a new CSRF token and resolves the issue. Do not just press the login button again as this will not generate a new authentication token.

---

## **Option 2**: Go Incognito / Private Mode

### 3. Use Incognito/Private Mode  

<video src="https://github.com/Edge-Hill-University-Web/Module-Resources/raw/refs/heads/main/WTE_privatemode.mov" controls width="640">
  Your browser does not support the video tag.  
  [Click here to download the video](https://github.com/Edge-Hill-University-Web/Module-Resources/raw/refs/heads/main/WTE_privatemode.mov)
</video>

For the best experience, open a **private or incognito window**:

- **Chrome:** `Ctrl + Shift + N` (Windows) or `⌘ + Shift + N` (Mac)  
- **Safari:** `⌘ + Shift + N`  
- **Edge:** `Ctrl + Shift + N`  

Then visit:  
👉 [https://teaching.computing.edgehill.ac.uk](https://teaching.computing.edgehill.ac.uk)

Log in again using your email and password. 

**Avoid when using the Web Teaching Environment https://www.edeghill.ac.uk!**

---
