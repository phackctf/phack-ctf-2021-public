<?php

# For debug, must remove later !!!
highlight_file ( __FILE__, false ); die();

$filename = "backup@" . date("m-d-Y") . ".zip";
$archive  = new ZipArchive();

if (!$archive->open("./dev-backups/" . $filename, (ZipArchive::CREATE | ZipArchive::OVERWRITE))) {
    die("Archive init failed");
}

$source = realpath("/mnt/mtp/device/029746912983");

$files = new RecursiveIteratorIterator(new RecursiveDirectoryIterator($source), RecursiveIteratorIterator::SELF_FIRST);

foreach ($files as $file) {

    if (in_array(substr($file, strrpos($file, '/') + 1), array('.', '..'))) {
        continue;
    }               

    $file = realpath($file);

    if (is_dir($file)) {
        $archive->addEmptyDir(str_replace($source . '/', '', $file . '/'));
    } elseif (is_file($file)) {
        $archive->addFromString(str_replace($source . '/', '', $file), file_get_contents($file));
    } else {
        die("Dealing with unknown file type.");
    }
}

$archive->close();

?>