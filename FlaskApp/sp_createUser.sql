CREATE OR REPLACE FUNCTION sp_createUser
   (    IN p_name CHAR(20),
        IN p_username CHAR(20),
        IN p_password CHAR(20)
   ) RETURNS setof record AS
$BODY$
begin
 IF (SELECT exists (SELECT * FROM table_user WHERE user_username = p_username)) THEN
        select 'Username Exists!!';
    ELSE
        INSERT INTO table_user(user_name, user_username, user_password) VALUES (p_name, p_username, p_password);    
    END IF;
return;
end;
$BODY$
LANGUAGE 'plpgsql';