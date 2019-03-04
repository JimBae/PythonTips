
# simple
f = open('test.jpg', 'r+')
data = f.read()
f.close()

# error가 open 직후에 발생하면 f.close()를 호출하지 않는다.
# 예외의 유무에 관계없이 파일을 닫으려면 with를 활용하여 감싼다.
with open('test.txt', 'r+') as f:
    data = f.read()

# r  : read-only
# r+ : read, write
# w  : 덮어쓰기
# a  : 파일에 더해서 쓰고 싶으면


# import io

# with open('photo.jpg', 'rb') as inf:
#     jpgdata = inf.data()

# if jpgdata.startwith(b'\xff\xd8'):
#     text = u'이 파일은 (%d 바이트 짜리) JPEG 파일입니다. \n'
# else:
#     text = u'이 파일은 (%d 바이트 짜리) 랜덤 파일입니다. \n'

# with io.open('summary.txt', 'w', encoding='UTF-8') as outf:
#     outf.write(text % len(jpgdata))

