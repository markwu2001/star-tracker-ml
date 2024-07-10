# This work is licensed under the MIT license.
# Copyright (c) 2013-2023 OpenMV LLC. All rights reserved.
# https://github.com/openmv/openmv/blob/master/LICENSE
#
# Global Shutter Triggered Mode Example
#
# This example shows off setting the global shutter camera into triggered mode. In triggered mode
# snapshot() controls EXACTLY when integration of the camera pixels start such that you can sync
# taking pictures to some external movement. Since the camera captures all pixels at the same time
# (as it is a global shutter camera versus a rolling shutter camera) movement in the image will
# only be captured for the integration time and not the integration time multiplied by the number
# of rows in the image. Additionally, sensor noise is reduced in triggered mode as the camera will
# not read out rows until after exposing which results in a higher quality image.
#
# That said, your maximum frame rate will be reduced by 2 to 3 as frames are no longer generated
# continuously by the camera and because you have to wait for the integration to finish before
# readout of the frame.

import sensor
import time

# Set the exposure time in us
EXPOSURE_MICROSECONDS = 800000
# Change this value to adjust the gain. Try 10.0/0/0.1/etc.
GAIN_SCALE = 0.2


sensor.reset()  # Reset and initialize the sensor.
sensor.set_pixformat(sensor.GRAYSCALE)  # Set pixel format to GRAYSCALE
sensor.set_framesize(sensor.WVGA2)  # Set frame size to largest resolution

# Print out the initial exposure time for comparison.
print("Initial exposure == %d" % sensor.get_exposure_us())

sensor.skip_frames(time=500)  # Wait for settings take effect.
clock = time.clock()  # Create a clock object to track the FPS.

# You have to turn automatic exposure control and automatic white balance off
# otherwise they will change the image exposure to undo any gain settings
# that you put in place...
sensor.set_auto_exposure(False)
sensor.set_auto_whitebal(False)
# Need to let the above settings get in...
sensor.skip_frames(time=500)

current_exposure_time_in_microseconds = sensor.get_exposure_us()
print("Current Exposure == %d" % current_exposure_time_in_microseconds)

# Auto exposure control (AEC) is enabled by default. Calling the below function
# disables sensor auto exposure control. The additionally "exposure_us"
# argument then overrides the auto exposure value after AEC is disabled.
sensor.set_auto_exposure(
    False, exposure_us=int(EXPOSURE_MICROSECONDS)
)

print("New exposure == %d" % sensor.get_exposure_us())
# sensor.get_exposure_us() returns the exact camera sensor exposure time
# in microseconds. However, this may be a different number than what was
# commanded because the sensor code converts the exposure time in microseconds
# to a row/pixel/clock time which doesn't perfectly match with microseconds...

# Print out the initial gain for comparison.
current_gain_in_decibels = sensor.get_gain_db()
print("Initial gain == %f db" % sensor.get_gain_db())

# Auto gain control (AGC) is enabled by default. Calling the below function
# disables sensor auto gain control. The additionally "gain_db"
# argument then overrides the auto gain value after AGC is disabled.
sensor.set_auto_gain(False, gain_db=current_gain_in_decibels * GAIN_SCALE)

print("New gain == %f db" % sensor.get_gain_db())

# Check what the coarse time is set to to make sure the exposure is actually being updated
sensor.__write_reg(0x0B, 32766) # Write to this register to just override the coarse exposure time
sensor.__write_reg(0xD2, 32766)

sensor.__write_reg(0xD5, 2046) # Write to this register to just override the fine exposure time
sensor.__write_reg(0xD8, 2046)
#sensor.__write_reg(0x0F, (1 << 0)) # Set camera to HDR Mode Context A
sensor.__write_reg(0x0F, (1 << 8)) # Set camera to HDR Mode Context B
print("HDR Status Reg: " , sensor.__read_reg(0x0F))
print("MT9V0XX_TOTAL_SHUTTER_WIDTH" , sensor.__read_reg(0x0B))
print("MT9V0X4_TOTAL_SHUTTER_WIDTH_B" , sensor.__read_reg(0xD2))
print("MT9V0X4_FINE_SHUTTER_WIDTH_TOTAL        " , sensor.__read_reg(0xD5))
print("MT9V0X4_FINE_SHUTTER_WIDTH_TOTAL_B        " , sensor.__read_reg(0xD8))

sensor.ioctl(sensor.IOCTL_SET_TRIGGERED_MODE, True)

while True:
    clock.tick()  # Update the FPS clock.
    img = sensor.snapshot()  # Take a picture and return the image.
    print("FPS: " , clock.fps())  # Note: OpenMV Cam runs about half as fast when connected
    print("Expose Time + Delay: " , 1/(clock.fps()))
    # to the IDE. The FPS should increase once disconnected.
