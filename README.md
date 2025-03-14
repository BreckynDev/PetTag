# PetTag
RFID COSC1030 Group Project

Login information for Raspberrypi COSC #5:
  Username: pettag
  Password: password1234

In the terminal window:
  directory: cd ~/pi-rfid [ENTER]
  source env/bin/activate [ENTER]

Link to full instruction document (includes how to set up the RFID, create a write and read file, and how to run the write and read files):
  https://pimylifeup.com/raspberry-pi-rfid-rc522/

To run the write file in order to write to the card/tag:
  python3 Write.py [ENTER]
    Place tag or card against the RFID
      "Written" will appear if successfully written to the card/tag

To run the read file in order to read the card/tag:
  python3 Read.py [ENTER]
    Place tag or card against the RFID
      "Read" will appear if successfully read from the card/tag
