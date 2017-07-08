cd ..
javac -d bin -sourcepath src -cp lib/twitter4j-core-4.0.4.jar:lib/twitter4j-stream-4.0.4.jar src/MultiThreadLocationAdvancedFillStreamFilterLinux02.java
java -Xmx5120M -cp bin:lib/twitter4j-core-4.0.4.jar:lib/twitter4j-stream-4.0.4.jar twitter4JBing.MultiThreadLocationAdvancedFillStreamFilterLinux02