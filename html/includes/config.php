<?php
// Get environment variables from Docker secrets
if (!function_exists('getenv_docker')) {
	function getenv_docker($env, $default) {
		if ($fileEnv = getenv($env . '_FILE')) {
			return rtrim(file_get_contents($fileEnv), "\r\n");
		}
		else if (($val = getenv($env)) !== false) {
			return $val;
		}
		else {
			return $default;
		}
	}
}

// Database configuration
define( 'DB_NAME', getenv_docker('DB_NAME', '') );
define( 'DB_USER', getenv_docker('DB_USER', '') );
define( 'DB_PASS', getenv_docker('DB_PASSWORD', '') );
define( 'DB_HOST', getenv_docker('DB_HOST', '') );
define( 'DB_PORT', getenv_docker('DB_PORT', '3306') );

try {
	$dbh = new PDO("mysql:host=" . DB_HOST . ";port=" . DB_PORT . ";dbname=" . DB_NAME, DB_USER, DB_PASS, array(PDO::MYSQL_ATTR_INIT_COMMAND => "SET NAMES 'utf8'"));
} catch (PDOException $e) {
	exit("Error: " . $e->getMessage());
}
