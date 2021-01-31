CREATE TABLE emails (
	id_oid text,
	sender TEXT,
	recipients TEXT,
	cc TEXT,
	text text,
	mid TEXT,
	fpath TEXT,
	bcc TEXT,
	replyto TEXT,
	ctype TEXT,
	fname TEXT,
	date TEXT,
	folder TEXT,
	subject TEXT,
	PRIMARY KEY (id_oid)
);

ALTER TABLE emails WITH GC_GRACE_SECONDS = 0;





