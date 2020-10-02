

CREATE DATABASE radius;

GRANT ALL PRIVILEGES ON radius.* TO radius@'%' IDENTIFIED BY 'qwe123' with grant option;
FLUSH PRIVILEGES;