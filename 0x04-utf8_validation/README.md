#### Validate utf-8 data points

<p> Unicode uses 8-bit code units and each character is encoded as 1 - 4 bytes. Therefore the are 4 main valid cases for the encoding and we can test for each in sequential conditional checks: </p>

- Check if byte-1 is between `0x00 - 0x7F`, these are valid `1-byte` UTF-8 chars.

- If byte-1 is between `0xC2 - 0xDF` byte-2 ranges `0x80 - 0xBF` then this is a valid `2-byte` char.

- Else if byte-1 is between `0xE0 - 0xEF` and the next 2 bytes start with `0x80` and are between `0x80 - 0xBF` then this is a valid `3-byte` char.

- Else if byte-1 is between `0xF0 - 0xF4` and the next 3 bytes start with `0x80` and are between `0x80 - 0xBF` then this is a valid `4-byte` char.

<p> Note the next 2 - 4 bytes starting with the same pattern is a built in feature to utf. Whenever the data is being streamed it is possible to start midstream which would cause `Hiragana` (unicode block) as the data would be decoded improperly. Instead when the encoder encounters these frames in the data it knows to discard them until it encounters the first byte which has a unique range (see above). </p>
