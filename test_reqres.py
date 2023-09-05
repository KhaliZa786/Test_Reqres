import pytest

def test_SingleUser(self):
    self.driver.get('https://reqres.in')
    self.driver.find_element(By.XPATH, '//*[@id="console"]/div[1]/ul/li[2]').click()
    self.driver.find_element(By.XPATH, '//*[@id="console"]/div[2]/div[1]/p/strong/a/span').click()
    time.sleep(1)
    t = self.driver.find_element(By.TAG_NAME, 'pre')
    check.equal(t.text,'{"data":{"id":2,"email":"janet.weaver@reqres.in","first_name":"Janet","last_name":"Weaver","avatar":"https://reqres.in/img/faces/2-image.jpg"},"support":{"url":"https://reqres.in/#support-heading","text":"To keep ReqRes free, contributions towards server costs are appreciated!"}}')

def test_ListUsers(self):
    self.driver.get('https://reqres.in')
    self.driver.find_element(By.XPATH, '//*[@id="console"]/div[1]/ul/li[1]').click()
    self.driver.find_element(By.XPATH, '//*[@id="console"]/div[2]/div[1]/p/strong/a/span').click()
    time.sleep(1)
    t = self.driver.find_element(By.TAG_NAME, 'pre')
    check.equal(t.text,'{"page":2,"per_page":6,"total":12,"total_pages":2,"data":[{"id":7,"email":"michael.lawson@reqres.in","first_name":"Michael","last_name":"Lawson","avatar":"https://reqres.in/img/faces/7-image.jpg"},{"id":8,"email":"lindsay.ferguson@reqres.in","first_name":"Lindsay","last_name":"Ferguson","avatar":"https://reqres.in/img/faces/8-image.jpg"},{"id":9,"email":"tobias.funke@reqres.in","first_name":"Tobias","last_name":"Funke","avatar":"https://reqres.in/img/faces/9-image.jpg"},{"id":10,"email":"byron.fields@reqres.in","first_name":"Byron","last_name":"Fields","avatar":"https://reqres.in/img/faces/10-image.jpg"},{"id":11,"email":"george.edwards@reqres.in","first_name":"George","last_name":"Edwards","avatar":"https://reqres.in/img/faces/11-image.jpg"},{"id":12,"email":"rachel.howell@reqres.in","first_name":"Rachel","last_name":"Howell","avatar":"https://reqres.in/img/faces/12-image.jpg"}],"support":{"url":"https://reqres.in/#support-heading","text":"To keep ReqRes free, contributions towards server costs are appreciated!"}}')

def test_SingleUserNotFound(self):
    self.driver.get('https://reqres.in')
    self.driver.find_element(By.XPATH, '//*[@id="console"]/div[1]/ul/li[3]').click()
    self.driver.find_element(By.XPATH, '//*[@id="console"]/div[2]/div[1]/p/strong/a/span').click()
    time.sleep(1)
    t = self.driver.find_element(By.TAG_NAME, 'pre')
    check.equal(t.text,'{}')

def test_ListResource(self):
    self.driver.get('https://reqres.in')
    self.driver.find_element(By.XPATH, '//*[@id="console"]/div[1]/ul/li[4]').click()
    self.driver.find_element(By.XPATH, '//*[@id="console"]/div[2]/div[1]/p/strong/a/span').click()
    time.sleep(1)
    t = self.driver.find_element(By.TAG_NAME, 'pre')
    check.equal(t.text,'{"page":1,"per_page":6,"total":12,"total_pages":2,"data":[{"id":1,"name":"cerulean","year":2000,"color":"#98B2D1","pantone_value":"15-4020"},{"id":2,"name":"fuchsia rose","year":2001,"color":"#C74375","pantone_value":"17-2031"},{"id":3,"name":"true red","year":2002,"color":"#BF1932","pantone_value":"19-1664"},{"id":4,"name":"aqua sky","year":2003,"color":"#7BC4C4","pantone_value":"14-4811"},{"id":5,"name":"tigerlily","year":2004,"color":"#E2583E","pantone_value":"17-1456"},{"id":6,"name":"blue turquoise","year":2005,"color":"#53B0AE","pantone_value":"15-5217"}],"support":{"url":"https://reqres.in/#support-heading","text":"To keep ReqRes free, contributions towards server costs are appreciated!"}}')

def test_SingleResource(self):
    self.driver.get('https://reqres.in')
    self.driver.find_element(By.XPATH, '//*[@id="console"]/div[1]/ul/li[5]').click()
    self.driver.find_element(By.XPATH, '//*[@id="console"]/div[2]/div[1]/p/strong/a/span').click()
    time.sleep(1)
    t = self.driver.find_element(By.TAG_NAME, 'pre')
    check.equal(t.text,'{"data":{"id":2,"name":"fuchsia rose","year":2001,"color":"#C74375","pantone_value":"17-2031"},"support":{"url":"https://reqres.in/#support-heading","text":"To keep ReqRes free, contributions towards server costs are appreciated!"}}')

def test_SingleResourceNotFound(self):
    self.driver.get('https://reqres.in')
    self.driver.find_element(By.XPATH, '//*[@id="console"]/div[1]/ul/li[6]/a').click()
    self.driver.find_element(By.XPATH, '//*[@id="console"]/div[2]/div[1]/p/strong/a/span').click()
    time.sleep(1)
    t = self.driver.find_element(By.TAG_NAME, 'pre')
    check.equal(t.text,'{}')

def test_Create(self):
    self.driver.get('https://reqres.in')
    self.driver.find_element(By.XPATH, '//*[@id="console"]/div[1]/ul/li[7]').click()
    self.driver.find_element(By.XPATH, '//*[@id="console"]/div[2]/div[1]/p/strong/a/span').click()
    time.sleep(1)
    t = self.driver.find_element(By.TAG_NAME, 'pre')
    check.equal(t.text,'{"page":1,"per_page":6,"total":12,"total_pages":2,"data":[{"id":1,"email":"george.bluth@reqres.in","first_name":"George","last_name":"Bluth","avatar":"https://reqres.in/img/faces/1-image.jpg"},{"id":2,"email":"janet.weaver@reqres.in","first_name":"Janet","last_name":"Weaver","avatar":"https://reqres.in/img/faces/2-image.jpg"},{"id":3,"email":"emma.wong@reqres.in","first_name":"Emma","last_name":"Wong","avatar":"https://reqres.in/img/faces/3-image.jpg"},{"id":4,"email":"eve.holt@reqres.in","first_name":"Eve","last_name":"Holt","avatar":"https://reqres.in/img/faces/4-image.jpg"},{"id":5,"email":"charles.morris@reqres.in","first_name":"Charles","last_name":"Morris","avatar":"https://reqres.in/img/faces/5-image.jpg"},{"id":6,"email":"tracey.ramos@reqres.in","first_name":"Tracey","last_name":"Ramos","avatar":"https://reqres.in/img/faces/6-image.jpg"}],"support":{"url":"https://reqres.in/#support-heading","text":"To keep ReqRes free, contributions towards server costs are appreciated!"}}')

def test_Update(self):
    self.driver.get('https://reqres.in')
    self.driver.find_element(By.XPATH, '//*[@id="console"]/div[1]/ul/li[8]').click()
    self.driver.find_element(By.XPATH, '//*[@id="console"]/div[2]/div[1]/p/strong/a/span').click()
    time.sleep(1)
    t = self.driver.find_element(By.TAG_NAME, 'pre')
    check.equal(t.text,'{"data":{"id":2,"email":"janet.weaver@reqres.in","first_name":"Janet","last_name":"Weaver","avatar":"https://reqres.in/img/faces/2-image.jpg"},"support":{"url":"https://reqres.in/#support-heading","text":"To keep ReqRes free, contributions towards server costs are appreciated!"}}')

def test_PatchUpdate(self):
    self.driver.get('https://reqres.in')
    self.driver.find_element(By.XPATH, '//*[@id="console"]/div[1]/ul/li[9]').click()
    self.driver.find_element(By.XPATH, '//*[@id="console"]/div[2]/div[1]/p/strong/a/span').click()
    time.sleep(1)
    t = self.driver.find_element(By.TAG_NAME, 'pre')
    check.equal(t.text,'{"data":{"id":2,"email":"janet.weaver@reqres.in","first_name":"Janet","last_name":"Weaver","avatar":"https://reqres.in/img/faces/2-image.jpg"},"support":{"url":"https://reqres.in/#support-heading","text":"To keep ReqRes free, contributions towards server costs are appreciated!"}}')

def test_Delete(self):
    self.driver.get('https://reqres.in')
    self.driver.find_element(By.XPATH, '//*[@id="console"]/div[1]/ul/li[10]').click()
    self.driver.find_element(By.XPATH, '//*[@id="console"]/div[2]/div[1]/p/strong/a/span').click()
    time.sleep(1)
    t = self.driver.find_element(By.TAG_NAME, 'pre')
    check.equal(t.text,'{"data":{"id":2,"email":"janet.weaver@reqres.in","first_name":"Janet","last_name":"Weaver","avatar":"https://reqres.in/img/faces/2-image.jpg"},"support":{"url":"https://reqres.in/#support-heading","text":"To keep ReqRes free, contributions towards server costs are appreciated!"}}')

def test_RegisterSuccessful(self):
    self.driver.get('https://reqres.in')
    self.driver.find_element(By.XPATH, '//*[@id="console"]/div[1]/ul/li[11]/a').click()
    self.driver.find_element(By.XPATH, '//*[@id="console"]/div[2]/div[1]/p/strong/a/span').click()
    time.sleep(1)
    t = self.driver.find_element(By.TAG_NAME, 'pre')
    check.equal(t.text,'{"page":1,"per_page":6,"total":12,"total_pages":2,"data":[{"id":1,"name":"cerulean","year":2000,"color":"#98B2D1","pantone_value":"15-4020"},{"id":2,"name":"fuchsia rose","year":2001,"color":"#C74375","pantone_value":"17-2031"},{"id":3,"name":"true red","year":2002,"color":"#BF1932","pantone_value":"19-1664"},{"id":4,"name":"aqua sky","year":2003,"color":"#7BC4C4","pantone_value":"14-4811"},{"id":5,"name":"tigerlily","year":2004,"color":"#E2583E","pantone_value":"17-1456"},{"id":6,"name":"blue turquoise","year":2005,"color":"#53B0AE","pantone_value":"15-5217"}],"support":{"url":"https://reqres.in/#support-heading","text":"To keep ReqRes free, contributions towards server costs are appreciated!"}}')

def test_RegisterUnsuccessful(self):
    self.driver.get('https://reqres.in')
    self.driver.find_element(By.XPATH, '//*[@id="console"]/div[1]/ul/li[12]').click()
    self.driver.find_element(By.XPATH, '//*[@id="console"]/div[2]/div[1]/p/strong/a/span').click()
    time.sleep(1)
    t = self.driver.find_element(By.TAG_NAME, 'pre')
    check.equal(t.text,'{"page":1,"per_page":6,"total":12,"total_pages":2,"data":[{"id":1,"name":"cerulean","year":2000,"color":"#98B2D1","pantone_value":"15-4020"},{"id":2,"name":"fuchsia rose","year":2001,"color":"#C74375","pantone_value":"17-2031"},{"id":3,"name":"true red","year":2002,"color":"#BF1932","pantone_value":"19-1664"},{"id":4,"name":"aqua sky","year":2003,"color":"#7BC4C4","pantone_value":"14-4811"},{"id":5,"name":"tigerlily","year":2004,"color":"#E2583E","pantone_value":"17-1456"},{"id":6,"name":"blue turquoise","year":2005,"color":"#53B0AE","pantone_value":"15-5217"}],"support":{"url":"https://reqres.in/#support-heading","text":"To keep ReqRes free, contributions towards server costs are appreciated!"}}')

def test_LoginSuccessful(self):
    self.driver.get('https://reqres.in')
    self.driver.find_element(By.XPATH, '//*[@id="console"]/div[1]/ul/li[13]a').click()
    self.driver.find_element(By.XPATH, '//*[@id="console"]/div[2]/div[1]/p/strong/a/span').click()
    time.sleep(1)
    t = self.driver.find_element(By.TAG_NAME, 'pre')
    check.equal(t.text,'{"page":1,"per_page":6,"total":12,"total_pages":2,"data":[{"id":1,"name":"cerulean","year":2000,"color":"#98B2D1","pantone_value":"15-4020"},{"id":2,"name":"fuchsia rose","year":2001,"color":"#C74375","pantone_value":"17-2031"},{"id":3,"name":"true red","year":2002,"color":"#BF1932","pantone_value":"19-1664"},{"id":4,"name":"aqua sky","year":2003,"color":"#7BC4C4","pantone_value":"14-4811"},{"id":5,"name":"tigerlily","year":2004,"color":"#E2583E","pantone_value":"17-1456"},{"id":6,"name":"blue turquoise","year":2005,"color":"#53B0AE","pantone_value":"15-5217"}],"support":{"url":"https://reqres.in/#support-heading","text":"To keep ReqRes free, contributions towards server costs are appreciated!"}}')

def test_LoginUnsuccessful(self):
    self.driver.get('https://reqres.in')
    self.driver.find_element(By.XPATH, '//*[@id="console"]/div[1]/ul/li[14]').click()
    self.driver.find_element(By.XPATH, '//*[@id="console"]/div[2]/div[1]/p/strong/a/span').click()
    time.sleep(1)
    t = self.driver.find_element(By.TAG_NAME, 'pre')
    check.equal(t.text,'{"page":1,"per_page":6,"total":12,"total_pages":2,"data":[{"id":1,"name":"cerulean","year":2000,"color":"#98B2D1","pantone_value":"15-4020"},{"id":2,"name":"fuchsia rose","year":2001,"color":"#C74375","pantone_value":"17-2031"},{"id":3,"name":"true red","year":2002,"color":"#BF1932","pantone_value":"19-1664"},{"id":4,"name":"aqua sky","year":2003,"color":"#7BC4C4","pantone_value":"14-4811"},{"id":5,"name":"tigerlily","year":2004,"color":"#E2583E","pantone_value":"17-1456"},{"id":6,"name":"blue turquoise","year":2005,"color":"#53B0AE","pantone_value":"15-5217"}],"support":{"url":"https://reqres.in/#support-heading","text":"To keep ReqRes free, contributions towards server costs are appreciated!"}}')

def test_DelayedResponse(self):
    self.driver.get('https://reqres.in')
    self.driver.find_element(By.XPATH, '//*[@id="console"]/div[1]/ul/li[15]/a').click()
    self.driver.find_element(By.XPATH, '//*[@id="console"]/div[2]/div[1]/p/strong/a/span').click()
    time.sleep(1)
    t = self.driver.find_element(By.TAG_NAME, 'pre')
    check.equal(t.text,'{"page":1,"per_page":6,"total":12,"total_pages":2,"data":[{"id":1,"email":"george.bluth@reqres.in","first_name":"George","last_name":"Bluth","avatar":"https://reqres.in/img/faces/1-image.jpg"},{"id":2,"email":"janet.weaver@reqres.in","first_name":"Janet","last_name":"Weaver","avatar":"https://reqres.in/img/faces/2-image.jpg"},{"id":3,"email":"emma.wong@reqres.in","first_name":"Emma","last_name":"Wong","avatar":"https://reqres.in/img/faces/3-image.jpg"},{"id":4,"email":"eve.holt@reqres.in","first_name":"Eve","last_name":"Holt","avatar":"https://reqres.in/img/faces/4-image.jpg"},{"id":5,"email":"charles.morris@reqres.in","first_name":"Charles","last_name":"Morris","avatar":"https://reqres.in/img/faces/5-image.jpg"},{"id":6,"email":"tracey.ramos@reqres.in","first_name":"Tracey","last_name":"Ramos","avatar":"https://reqres.in/img/faces/6-image.jpg"}],"support":{"url":"https://reqres.in/#support-heading","text":"To keep ReqRes free, contributions towards server costs are appreciated!"}}')