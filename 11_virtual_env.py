# install
#> pip install virtualenv

# set virtualenv
#> virtualenv myenv
#> source myenv/bin/activate

# virtualenv를 생성하는 동안 virtialenv가 시스템의 site-packages에 있는 패키지들을 사용하거나,
# virtualenv의 site-packages에 있는 패키지들을 설치할지를 결정해야한다. 
# 기본적으로는 virtualenv는 전역 사이트 패키지에 대한 엑세스 권한을 부여하지 않는다. 
# virtualenv가 시스템 site-packages에 엑세스하게 하려면 
# 다음과 같이 virtualenv를 만들때 --system-site-packages 스위치를 사용해야한다.
#
#> virtualenv --system-site-packages mycoolvenv

# deactivate command
#> deactivate

