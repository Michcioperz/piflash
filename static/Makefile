clean:
	rm main.bin main.hex

%.bin: %.cpp
	avr-g++ -mmcu=atmega8 $^ -o $@

%.hex: %.bin
	avr-objcopy -O ihex $^ $@

%.flash: %.hex
	sudo avrdude -c usbasp -p m8 -U flash:w:$^
