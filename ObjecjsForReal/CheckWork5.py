from Work5 import HardDisk

Disk = HardDisk(19,19)

Disk.addFile(12)
Disk.addFile(13)
Disk.addFile(50)
Disk.addFile(25)
Disk.delFile(34)

print(Disk.Show())