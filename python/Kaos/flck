#!/usr/bin/ruby -w
# encode: ISO_8859_1
# Define Colors
# This Class Is Not Currently Used By FlCk
class String
  def colorize(color_code)
    "\e[#{color_code}m#{self}\e{0m"
  end
  def red
    colorize(31)
  end
  def green
    colorize(32)
  end
  def yellow
    colorize(33)
  end
  def blue
    colorize(34)
  end
  def pink
    colorize(35)
  end
  def light_blue
    colorize(36)
  end
end
# Allow User To Parse File From COmmand Line
ARGV.each { |filename|
# Check To See If User Is Asking For Help
if filename == '--help' || filename == '-h'
  puts "Usage: flck [file/dir]\nSee: man flck"
# Check To See If File Exists
else
# If File Exists, Run Remaining Tests
# Else Skip To End
  if File::exist?( filename )
    file = File.open( filename )
# Check To See If File Name Is An Existing File
    if File.file?( file )
      chkfile = "True"
    else
      chkfile = "False"
    end
# Check To See If File Name Is An Existing Directory
    if File::directory?( file )
      dir = "True"
    else
      dir = "False"
    end
# Check File Permissions
# Check To See If File Is Readable
    if File.readable?( file )
      readable = "True"
    else
      readable = "False"
    end
# Check To See If File Is Writable
    if File.writable?( file )
      writeable = "True"
    else
      writeable = "False"
    end
# Check To See If File Is Executable
    if File.executable?( file )
      exec = "True"
    else
      exec = "False"
    end
# Check To See If File Is Zero Size
    if File.zero?( file )
      zerosize = "True"
    else
      zerosize = "False"
    end
# Check File Path
    path = File::expand_path( file ).to_s
# Check File Size
    size = File.size?( file ).to_s
# Check File Type
    ftype = File::ftype( file )
# Check To See When File Was Created
    create = File::ctime( file ).to_s
# Check to See When File Was Last Modified
    mod = File::mtime( file ).to_s
# Check To See When File Was Last Accessed
    lstaccess = File::atime( file ).to_s
# Print Output Of Tests To Screen
    puts "##################################################"
    puts "#  [Name]: "+ filename
    puts "#  [Exsisting File]: "+ chkfile
    puts "#  [Exsisting Directory]: "+dir
    puts "#  [Path]: "+path
    puts "#  [File Type]: "+ftype
    puts "#  [Created]: "+create
    puts "#  [Modified]: "+mod
    puts "#  [Last Accessed]: "+lstaccess
    puts "#  [Readable]: "+readable
    puts "#  [Writeable]: "+writeable
    puts "#  [Executable]: "+exec
    puts "#  [Zero Size]: "+zerosize
    puts "#  [Size]: "+size
    puts "##################################################"
  else
# If The File Does Not Exist
# Print Error Message
    print "That File Does Not Exist!!!\n"
  end
end
}
