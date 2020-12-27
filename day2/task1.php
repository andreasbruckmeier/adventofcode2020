<?php
$correct = 0;
foreach (file('input.txt') as $line) {
  list($policy, $character, $password) = explode(" ", $line);
  list($policy_min, $policy_max) = explode('-', $policy);
  $count = substr_count(trim($password), substr($character, 0, 1));
  if (($policy_min <= $count) && ($count <= $policy_max))
    ++$correct;
}
print($correct);
