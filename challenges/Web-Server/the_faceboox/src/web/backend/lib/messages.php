<?php

include 'users.php';

class Message {
  public $from = 0;
  public $to   = 0;
  public $text = "";

  public function __construct($from, $to, $text)
  {
    $this->from = $from;
    $this->to   = $to;
    $this->text = $text;
  }

  public function from() {
    return UserDB::get($this->from)['name'];
  }

  public function to() {
    return UserDB::get($this->to)['name'];
  }
}

class MessageDB {
  private static $messages = array();

  public static function add($from, $to, $text) {
    array_push( self::$messages, new Message($from, $to, $text) );
  }

  public static function get($id) {
    $dm = array();

    foreach(self::$messages as $message) {
      if ($message->to == $id) {
        array_push($dm, $message);
      }
    }

    return $dm;
  }
}

MessageDB::add(3, 1, "Hey Mike ! Will U join us tonight for Laura's boyfriend secret party ?? Gonna be lit ;)");
MessageDB::add(2, 1, "Don't forget to bring the Watibulle, cya tonight :p");
MessageDB::add(1, 3, "Will be there tonight ofc !! :D");
MessageDB::add(1, 2, "Dooon't worry, it's in my bag already ^_^");
MessageDB::add(2, 3, "Hope you and Mike are coming tonight ;-)");
MessageDB::add(3, 2, "YES WE ARE MAM' ! :p");
MessageDB::add(5, 4, "Hey Rachel ! I've juste reset the Fox News press account password as you requested. <br><br>The new password is : jKslA54sSjdAjs.<br><br>Make sure to change it next time you login ! :)");
MessageDB::add(5, 5, "Congrats, you h4cked me ! The flag is <b>PHACK{1Nt3rnet_C'e7ait_m1euX_Av@nt!:(}</b>");
MessageDB::add(5, 5, "Reminder : Answering to this guy from Cambridge Analytica, or he won't stop calling me...");

?>