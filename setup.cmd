SET comport=COM4
SET firmware=firmware\esp32-idf3-20190529-v1.11.bin

esptool --port %comport% erase_flash
esptool --chip esp32 --port %comport% write_flash -z 0x1000 %firmware%