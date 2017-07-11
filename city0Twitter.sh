# /usr/bin/sh
cd ..
javac -d bin -sourcepath src -cp lib/twitter4j-core-4.0.4.jar:lib/twitter4j-stream-4.0.4.jar src/MultiThreadLocationAdvancedFillStreamFilterLinux00.java
java -Xmx1800M -cp bin:lib/twitter4j-core-4.0.4.jar:lib/twitter4j-stream-4.0.4.jar twitter4JBing.MultiThreadLocationAdvancedFillStreamFilterLinux00
#java -Xmx5120M -cp bin:lib/twitter4j-core-4.0.4.jar:lib/twitter4j-stream-4.0.4.jar twitter4JBing.MultiThreadLocationAdvancedFillStreamFilterLinux00
