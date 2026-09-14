--Crear y Popular la DB

--1. Crear el schema
CREATE SCHEMA IF NOT EXISTS lyfter_car_rental;

--2. Crear la tabla de usuarios
DROP TABLE IF EXISTS lyfter_car_rental.usuarios CASCADE;

CREATE TABLE lyfter_car_rental.usuarios (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(100) NOT NULL,
    last_name VARCHAR(150) NOT NULL,
    email VARCHAR(150) NOT NULL UNIQUE,
    username VARCHAR(50) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL,
    birthdate DATE NOT NULL,
    state_account VARCHAR(20) NOT NULL DEFAULT 'activo' CHECK (state_account IN ('activo', 'inactivo', 'suspendido'))
);
--3. Popular la tabla con 150 usuarios
insert into lyfter_car_rental.usuarios (id, first_name, last_name, email, username, password, birthdate, state_account) values (1, 'Tamqrah', 'Matthessen', 'tmatthessen0@vimeo.com', 'tmatthessen0', 'bF6*npWf/IJQA', '7/16/2025', 'inactivo');
insert into lyfter_car_rental.usuarios (id, first_name, last_name, email, username, password, birthdate, state_account) values (2, 'Sheridan', 'Rillatt', 'srillatt1@php.net', 'srillatt1', 'jA1''G6`*', '7/23/2025', 'activo');
insert into lyfter_car_rental.usuarios (id, first_name, last_name, email, username, password, birthdate, state_account) values (3, 'Aldridge', 'Doubleday', 'adoubleday2@360.cn', 'adoubleday2', 'jZ6+zm"to4+R%K', '6/12/2026', 'inactivo');
insert into lyfter_car_rental.usuarios (id, first_name, last_name, email, username, password, birthdate, state_account) values (4, 'Carlota', 'Pibsworth', 'cpibsworth3@seattletimes.com', 'cpibsworth3', 'gK9'')m`YqI.ihZ', '7/11/2026', 'suspendido');
insert into lyfter_car_rental.usuarios (id, first_name, last_name, email, username, password, birthdate, state_account) values (5, 'Evelin', 'Dayly', 'edayly4@imageshack.us', 'edayly4', 'aR7=sotI+''L,p.z', '11/29/2024', 'inactivo');
insert into lyfter_car_rental.usuarios (id, first_name, last_name, email, username, password, birthdate, state_account) values (6, 'Stanislaw', 'McCrillis', 'smccrillis5@tripod.com', 'smccrillis5', 'rP0%PK3"}Hw1V34n', '8/14/2025', 'activo');
insert into lyfter_car_rental.usuarios (id, first_name, last_name, email, username, password, birthdate, state_account) values (7, 'Imojean', 'Tytler', 'itytler6@networkadvertising.org', 'itytler6', 'dB9/km${RD>_"+', '1/2/2025', 'activo');
insert into lyfter_car_rental.usuarios (id, first_name, last_name, email, username, password, birthdate, state_account) values (8, 'Benjamen', 'Allett', 'ballett7@canalblog.com', 'ballett7', 'oE6\#\Bf79P', '1/24/2025', 'activo');
insert into lyfter_car_rental.usuarios (id, first_name, last_name, email, username, password, birthdate, state_account) values (9, 'Rex', 'Proom', 'rproom8@reference.com', 'rproom8', 'pH2`Q(tQeGxit', '9/18/2024', 'activo');
insert into lyfter_car_rental.usuarios (id, first_name, last_name, email, username, password, birthdate, state_account) values (10, 'Melesa', 'Folbigg', 'mfolbigg9@mysql.com', 'mfolbigg9', 'yD7.o_vR', '10/26/2025', 'suspendido');
insert into lyfter_car_rental.usuarios (id, first_name, last_name, email, username, password, birthdate, state_account) values (11, 'Tuckie', 'Havick', 'thavicka@amazon.com', 'thavicka', 'hJ4?VhC<EWJ', '8/27/2025', 'inactivo');
insert into lyfter_car_rental.usuarios (id, first_name, last_name, email, username, password, birthdate, state_account) values (12, 'Allina', 'Broadway', 'abroadwayb@furl.net', 'abroadwayb', 'yV2&0HdW}7C>M', '1/20/2025', 'suspendido');
insert into lyfter_car_rental.usuarios (id, first_name, last_name, email, username, password, birthdate, state_account) values (13, 'Fair', 'Aucock', 'faucockc@wix.com', 'faucockc', 'wE0`/RY+IRr', '7/25/2024', 'suspendido');
insert into lyfter_car_rental.usuarios (id, first_name, last_name, email, username, password, birthdate, state_account) values (14, 'Tori', 'McKeeman', 'tmckeemand@google.cn', 'tmckeemand', 'nL7#bD+<M?f', '3/16/2025', 'activo');
insert into lyfter_car_rental.usuarios (id, first_name, last_name, email, username, password, birthdate, state_account) values (15, 'Loraine', 'Attarge', 'lattargee@cnet.com', 'lattargee', 'eW4}ljZQDE''!hSr', '5/15/2025', 'suspendido');
insert into lyfter_car_rental.usuarios (id, first_name, last_name, email, username, password, birthdate, state_account) values (16, 'Leola', 'Bagwell', 'lbagwellf@fda.gov', 'lbagwellf', 'uF1*1B4m', '9/13/2024', 'suspendido');
insert into lyfter_car_rental.usuarios (id, first_name, last_name, email, username, password, birthdate, state_account) values (17, 'Avivah', 'Coneron', 'aconerong@dmoz.org', 'aconerong', 'jT3{$?<p7Sw+Y', '8/13/2024', 'activo');
insert into lyfter_car_rental.usuarios (id, first_name, last_name, email, username, password, birthdate, state_account) values (18, 'Benedikta', 'Carillo', 'bcarilloh@imgur.com', 'bcarilloh', 'gR3\em2xSt?e', '6/16/2026', 'suspendido');
insert into lyfter_car_rental.usuarios (id, first_name, last_name, email, username, password, birthdate, state_account) values (19, 'Patton', 'Verring', 'pverringi@utexas.edu', 'pverringi', 'yV9\_4RtCp', '3/27/2025', 'inactivo');
insert into lyfter_car_rental.usuarios (id, first_name, last_name, email, username, password, birthdate, state_account) values (20, 'Margareta', 'Ragat', 'mragatj@harvard.edu', 'mragatj', 'yR5_QsJsr,U$', '10/13/2025', 'suspendido');
insert into lyfter_car_rental.usuarios (id, first_name, last_name, email, username, password, birthdate, state_account) values (21, 'Cam', 'Jouannin', 'cjouannink@people.com.cn', 'cjouannink', 'aL7&.J.gN7M*S', '1/1/2026', 'activo');
insert into lyfter_car_rental.usuarios (id, first_name, last_name, email, username, password, birthdate, state_account) values (22, 'Conway', 'Wathell', 'cwathelll@bandcamp.com', 'cwathelll', 'sK8~|B@#''P/,u7', '8/7/2026', 'inactivo');
insert into lyfter_car_rental.usuarios (id, first_name, last_name, email, username, password, birthdate, state_account) values (23, 'Zondra', 'Bartlet', 'zbartletm@miibeian.gov.cn', 'zbartletm', 'aY0!\CrJW}XsX{O', '3/3/2025', 'suspendido');
insert into lyfter_car_rental.usuarios (id, first_name, last_name, email, username, password, birthdate, state_account) values (24, 'Brandy', 'Swoffer', 'bswoffern@va.gov', 'bswoffern', 'jX9{&gttSha.l*_', '2/21/2026', 'suspendido');
insert into lyfter_car_rental.usuarios (id, first_name, last_name, email, username, password, birthdate, state_account) values (25, 'Teresina', 'Kittel', 'tkittelo@ehow.com', 'tkittelo', 'lW7(tk_.,tF6', '7/8/2025', 'inactivo');
insert into lyfter_car_rental.usuarios (id, first_name, last_name, email, username, password, birthdate, state_account) values (26, 'Jermain', 'Undy', 'jundyp@google.de', 'jundyp', 'aA0&@ti}!.fNcx', '1/24/2026', 'activo');
insert into lyfter_car_rental.usuarios (id, first_name, last_name, email, username, password, birthdate, state_account) values (27, 'Barri', 'Sydenham', 'bsydenhamq@webeden.co.uk', 'bsydenhamq', 'eL8+w26"', '2/23/2026', 'suspendido');
insert into lyfter_car_rental.usuarios (id, first_name, last_name, email, username, password, birthdate, state_account) values (28, 'Eydie', 'Dearan', 'edearanr@prlog.org', 'edearanr', 'qE1\%<g*9k}=j', '6/5/2025', 'inactivo');
insert into lyfter_car_rental.usuarios (id, first_name, last_name, email, username, password, birthdate, state_account) values (29, 'Tanner', 'Scullard', 'tscullards@vkontakte.ru', 'tscullards', 'vL1,o*>r,QRd', '11/25/2025', 'suspendido');
insert into lyfter_car_rental.usuarios (id, first_name, last_name, email, username, password, birthdate, state_account) values (30, 'Frannie', 'Gregorin', 'fgregorint@google.co.uk', 'fgregorint', 'bA8)9owd?bo0%UO', '2/26/2026', 'activo');
insert into lyfter_car_rental.usuarios (id, first_name, last_name, email, username, password, birthdate, state_account) values (31, 'Zak', 'Simnell', 'zsimnellu@devhub.com', 'zsimnellu', 'jH6=`Z`#1WTd%O', '3/2/2025', 'inactivo');
insert into lyfter_car_rental.usuarios (id, first_name, last_name, email, username, password, birthdate, state_account) values (32, 'Garrik', 'Millier', 'gmillierv@utexas.edu', 'gmillierv', 'yI6\R!''t}', '7/5/2024', 'suspendido');
insert into lyfter_car_rental.usuarios (id, first_name, last_name, email, username, password, birthdate, state_account) values (33, 'Nelly', 'Giamitti', 'ngiamittiw@parallels.com', 'ngiamittiw', 'gS0(h5_sWnY"o', '5/6/2025', 'activo');
insert into lyfter_car_rental.usuarios (id, first_name, last_name, email, username, password, birthdate, state_account) values (34, 'Thalia', 'Room', 'troomx@icio.us', 'troomx', 'nA1+rL56<.Vg)', '2/6/2026', 'suspendido');
insert into lyfter_car_rental.usuarios (id, first_name, last_name, email, username, password, birthdate, state_account) values (35, 'Mair', 'Crichten', 'mcrichteny@europa.eu', 'mcrichteny', 'aX2+pZ#qGE', '4/3/2026', 'suspendido');
insert into lyfter_car_rental.usuarios (id, first_name, last_name, email, username, password, birthdate, state_account) values (36, 'Findlay', 'Dadds', 'fdaddsz@illinois.edu', 'fdaddsz', 'aU3(D$s({Mxp', '10/9/2024', 'activo');
insert into lyfter_car_rental.usuarios (id, first_name, last_name, email, username, password, birthdate, state_account) values (37, 'Claudio', 'Bradnocke', 'cbradnocke10@delicious.com', 'cbradnocke10', 'nX2/Kh''_vF', '8/31/2025', 'activo');
insert into lyfter_car_rental.usuarios (id, first_name, last_name, email, username, password, birthdate, state_account) values (38, 'Mikaela', 'Swayton', 'mswayton11@squarespace.com', 'mswayton11', 'aN9|rf2UzAsQH', '4/16/2025', 'inactivo');
insert into lyfter_car_rental.usuarios (id, first_name, last_name, email, username, password, birthdate, state_account) values (39, 'Glenn', 'Bengle', 'gbengle12@amazonaws.com', 'gbengle12', 'jL0\Z|D''i)o/}', '5/10/2026', 'activo');
insert into lyfter_car_rental.usuarios (id, first_name, last_name, email, username, password, birthdate, state_account) values (40, 'Gillie', 'Kayzer', 'gkayzer13@yellowbook.com', 'gkayzer13', 'pU8$1''|x', '12/11/2024', 'activo');
insert into lyfter_car_rental.usuarios (id, first_name, last_name, email, username, password, birthdate, state_account) values (41, 'Heath', 'Gheraldi', 'hgheraldi14@alibaba.com', 'hgheraldi14', 'xU0\QJxkE<?s##z$', '4/24/2025', 'activo');
insert into lyfter_car_rental.usuarios (id, first_name, last_name, email, username, password, birthdate, state_account) values (42, 'Cal', 'McCreedy', 'cmccreedy15@baidu.com', 'cmccreedy15', 'vN6@{V<1.', '9/8/2025', 'suspendido');
insert into lyfter_car_rental.usuarios (id, first_name, last_name, email, username, password, birthdate, state_account) values (43, 'Agathe', 'Rilton', 'arilton16@squidoo.com', 'arilton16', 'rQ6|Ib6sJ$''1', '10/22/2025', 'activo');
insert into lyfter_car_rental.usuarios (id, first_name, last_name, email, username, password, birthdate, state_account) values (44, 'Francis', 'Hefner', 'fhefner17@shutterfly.com', 'fhefner17', 'aE2&$Grl', '9/7/2024', 'inactivo');
insert into lyfter_car_rental.usuarios (id, first_name, last_name, email, username, password, birthdate, state_account) values (45, 'Aleta', 'Wolvey', 'awolvey18@tumblr.com', 'awolvey18', 'lG6/d6c+V_', '5/21/2025', 'suspendido');
insert into lyfter_car_rental.usuarios (id, first_name, last_name, email, username, password, birthdate, state_account) values (46, 'Brooks', 'Blazhevich', 'bblazhevich19@nymag.com', 'bblazhevich19', 'nU9~zE,p1!JeIuK', '10/4/2025', 'inactivo');
insert into lyfter_car_rental.usuarios (id, first_name, last_name, email, username, password, birthdate, state_account) values (47, 'Jerrie', 'Kimbrough', 'jkimbrough1a@mysql.com', 'jkimbrough1a', 'yY3(&0U5rx!I@p', '3/16/2026', 'activo');
insert into lyfter_car_rental.usuarios (id, first_name, last_name, email, username, password, birthdate, state_account) values (48, 'Carmelia', 'Farfull', 'cfarfull1b@com.com', 'cfarfull1b', 'sD4$q+nFO', '5/1/2025', 'inactivo');
insert into lyfter_car_rental.usuarios (id, first_name, last_name, email, username, password, birthdate, state_account) values (49, 'Charissa', 'Grabban', 'cgrabban1c@tripadvisor.com', 'cgrabban1c', 'nR5@aX>f!a,3O*', '6/4/2026', 'inactivo');
insert into lyfter_car_rental.usuarios (id, first_name, last_name, email, username, password, birthdate, state_account) values (50, 'Glenna', 'Culshew', 'gculshew1d@thetimes.co.uk', 'gculshew1d', 'aN4//h7SG<.0CJC', '3/24/2026', 'suspendido');
insert into lyfter_car_rental.usuarios (id, first_name, last_name, email, username, password, birthdate, state_account) values (51, 'Chrysa', 'Whiteway', 'cwhiteway1e@pbs.org', 'cwhiteway1e', 'jQ0<`|PkM(nD/<', '10/25/2025', 'suspendido');
insert into lyfter_car_rental.usuarios (id, first_name, last_name, email, username, password, birthdate, state_account) values (52, 'Jocelin', 'Insall', 'jinsall1f@reuters.com', 'jinsall1f', 'vR1@CJdw)@', '12/21/2024', 'inactivo');
insert into lyfter_car_rental.usuarios (id, first_name, last_name, email, username, password, birthdate, state_account) values (53, 'Ange', 'Rouchy', 'arouchy1g@digg.com', 'arouchy1g', 'kZ6~DU&HgB', '7/4/2026', 'activo');
insert into lyfter_car_rental.usuarios (id, first_name, last_name, email, username, password, birthdate, state_account) values (54, 'Mikael', 'Blackledge', 'mblackledge1h@elegantthemes.com', 'mblackledge1h', 'oL1`ehqME', '3/14/2025', 'suspendido');
insert into lyfter_car_rental.usuarios (id, first_name, last_name, email, username, password, birthdate, state_account) values (55, 'Boyce', 'Robins', 'brobins1i@rediff.com', 'brobins1i', 'lR9?Wwo*B#.b<s|', '4/15/2025', 'suspendido');
insert into lyfter_car_rental.usuarios (id, first_name, last_name, email, username, password, birthdate, state_account) values (56, 'Neille', 'Crudgington', 'ncrudgington1j@dmoz.org', 'ncrudgington1j', 'lY6!oH&8U%#<@Y', '8/10/2024', 'inactivo');
insert into lyfter_car_rental.usuarios (id, first_name, last_name, email, username, password, birthdate, state_account) values (57, 'Derick', 'Balfre', 'dbalfre1k@51.la', 'dbalfre1k', 'vU5%0**BbQ@z<mZ', '5/22/2025', 'activo');
insert into lyfter_car_rental.usuarios (id, first_name, last_name, email, username, password, birthdate, state_account) values (58, 'Melinda', 'Northfield', 'mnorthfield1l@ocn.ne.jp', 'mnorthfield1l', 'wW2,Kui!>vU', '10/4/2025', 'inactivo');
insert into lyfter_car_rental.usuarios (id, first_name, last_name, email, username, password, birthdate, state_account) values (59, 'Teressa', 'Findlater', 'tfindlater1m@pinterest.com', 'tfindlater1m', 'mT8?_)p9x3!', '4/8/2025', 'activo');
insert into lyfter_car_rental.usuarios (id, first_name, last_name, email, username, password, birthdate, state_account) values (60, 'Sharla', 'Atlee', 'satlee1n@github.io', 'satlee1n', 'nE3|esSO3=/j?"4', '4/24/2025', 'suspendido');
insert into lyfter_car_rental.usuarios (id, first_name, last_name, email, username, password, birthdate, state_account) values (61, 'Jemie', 'Grent', 'jgrent1o@ezinearticles.com', 'jgrent1o', 'rC7#3GgUMx7R', '4/30/2025', 'activo');
insert into lyfter_car_rental.usuarios (id, first_name, last_name, email, username, password, birthdate, state_account) values (62, 'Delmar', 'Duiguid', 'dduiguid1p@soundcloud.com', 'dduiguid1p', 'tR9)8YZVJ"\V!', '1/24/2025', 'inactivo');
insert into lyfter_car_rental.usuarios (id, first_name, last_name, email, username, password, birthdate, state_account) values (63, 'Dalis', 'Schneider', 'dschneider1q@ucla.edu', 'dschneider1q', 'gL8<~79)', '2/20/2025', 'activo');
insert into lyfter_car_rental.usuarios (id, first_name, last_name, email, username, password, birthdate, state_account) values (64, 'Anatole', 'Steen', 'asteen1r@sciencedaily.com', 'asteen1r', 'cB9"hPvCU|', '7/13/2025', 'inactivo');
insert into lyfter_car_rental.usuarios (id, first_name, last_name, email, username, password, birthdate, state_account) values (65, 'Fay', 'McKinstry', 'fmckinstry1s@nifty.com', 'fmckinstry1s', 'qT0`?K?4=', '2/11/2025', 'suspendido');
insert into lyfter_car_rental.usuarios (id, first_name, last_name, email, username, password, birthdate, state_account) values (66, 'Shelton', 'Lyngsted', 'slyngsted1t@e-recht24.de', 'slyngsted1t', 'wB9$?ywll', '7/11/2026', 'inactivo');
insert into lyfter_car_rental.usuarios (id, first_name, last_name, email, username, password, birthdate, state_account) values (67, 'Audrey', 'Shall', 'ashall1u@state.gov', 'ashall1u', 'qC2{Sf!6', '3/2/2026', 'inactivo');
insert into lyfter_car_rental.usuarios (id, first_name, last_name, email, username, password, birthdate, state_account) values (68, 'Brit', 'Scola', 'bscola1v@loc.gov', 'bscola1v', 'zR2~X0PH1', '3/10/2025', 'activo');
insert into lyfter_car_rental.usuarios (id, first_name, last_name, email, username, password, birthdate, state_account) values (69, 'Angel', 'Cutchey', 'acutchey1w@elegantthemes.com', 'acutchey1w', 'jK2{ncQP', '12/10/2024', 'activo');
insert into lyfter_car_rental.usuarios (id, first_name, last_name, email, username, password, birthdate, state_account) values (70, 'Ransom', 'Wimms', 'rwimms1x@cpanel.net', 'rwimms1x', 'sL6?06O{bk''Wp,GJ', '2/19/2026', 'suspendido');
insert into lyfter_car_rental.usuarios (id, first_name, last_name, email, username, password, birthdate, state_account) values (71, 'Teddie', 'Le Moucheux', 'tlemoucheux1y@myspace.com', 'tlemoucheux1y', 'tV8>ncNxj', '4/8/2025', 'suspendido');
insert into lyfter_car_rental.usuarios (id, first_name, last_name, email, username, password, birthdate, state_account) values (72, 'Alisha', 'Amberson', 'aamberson1z@jiathis.com', 'aamberson1z', 'vH2*op\"x3KLsL', '7/29/2026', 'inactivo');
insert into lyfter_car_rental.usuarios (id, first_name, last_name, email, username, password, birthdate, state_account) values (73, 'Lonni', 'Antonomoli', 'lantonomoli20@prlog.org', 'lantonomoli20', 'vT9}N+UNI9.a1$n', '4/30/2026', 'suspendido');
insert into lyfter_car_rental.usuarios (id, first_name, last_name, email, username, password, birthdate, state_account) values (74, 'Catherin', 'Meineking', 'cmeineking21@arstechnica.com', 'cmeineking21', 'nQ1}e8I?xj4p0#f,', '6/19/2024', 'suspendido');
insert into lyfter_car_rental.usuarios (id, first_name, last_name, email, username, password, birthdate, state_account) values (75, 'Ode', 'Aulsford', 'oaulsford22@google.com.au', 'oaulsford22', 'mJ1="zfJ#ls', '8/13/2026', 'suspendido');
insert into lyfter_car_rental.usuarios (id, first_name, last_name, email, username, password, birthdate, state_account) values (76, 'Aurelia', 'Duckerin', 'aduckerin23@upenn.edu', 'aduckerin23', 'jV9#nH|TQ.r0', '11/11/2025', 'inactivo');
insert into lyfter_car_rental.usuarios (id, first_name, last_name, email, username, password, birthdate, state_account) values (77, 'Tallulah', 'Caffrey', 'tcaffrey24@apple.com', 'tcaffrey24', 'rH6,WX`CX', '3/12/2026', 'activo');
insert into lyfter_car_rental.usuarios (id, first_name, last_name, email, username, password, birthdate, state_account) values (78, 'Harlene', 'Blance', 'hblance25@amazon.com', 'hblance25', 'mG6@tz?qL_N1D09', '9/28/2025', 'inactivo');
insert into lyfter_car_rental.usuarios (id, first_name, last_name, email, username, password, birthdate, state_account) values (79, 'Gerda', 'Cleife', 'gcleife26@abc.net.au', 'gcleife26', 'lQ2/0D"f', '12/22/2024', 'suspendido');
insert into lyfter_car_rental.usuarios (id, first_name, last_name, email, username, password, birthdate, state_account) values (80, 'Tuckie', 'Bernard', 'tbernard27@hostgator.com', 'tbernard27', 'xG9{mDGwi', '1/26/2025', 'suspendido');
insert into lyfter_car_rental.usuarios (id, first_name, last_name, email, username, password, birthdate, state_account) values (81, 'Darnall', 'Gallafant', 'dgallafant28@rambler.ru', 'dgallafant28', 'fA7{itlUGzh42', '8/20/2025', 'activo');
insert into lyfter_car_rental.usuarios (id, first_name, last_name, email, username, password, birthdate, state_account) values (82, 'Worden', 'Lambertson', 'wlambertson29@youku.com', 'wlambertson29', 'tF1>0G\Pjw8,G', '8/18/2024', 'suspendido');
insert into lyfter_car_rental.usuarios (id, first_name, last_name, email, username, password, birthdate, state_account) values (83, 'Denney', 'Mallebone', 'dmallebone2a@cbc.ca', 'dmallebone2a', 'kW1=IQ1I', '2/9/2026', 'activo');
insert into lyfter_car_rental.usuarios (id, first_name, last_name, email, username, password, birthdate, state_account) values (84, 'Heywood', 'Standingford', 'hstandingford2b@moonfruit.com', 'hstandingford2b', 'yN2@64OQ', '10/15/2024', 'inactivo');
insert into lyfter_car_rental.usuarios (id, first_name, last_name, email, username, password, birthdate, state_account) values (85, 'Paola', 'Josephov', 'pjosephov2c@livejournal.com', 'pjosephov2c', 'kV9/gvzsNE#,>!pf', '2/27/2025', 'inactivo');
insert into lyfter_car_rental.usuarios (id, first_name, last_name, email, username, password, birthdate, state_account) values (86, 'Madelina', 'Brosetti', 'mbrosetti2d@netlog.com', 'mbrosetti2d', 'oA1)T3K{xp', '1/11/2026', 'activo');
insert into lyfter_car_rental.usuarios (id, first_name, last_name, email, username, password, birthdate, state_account) values (87, 'Julissa', 'Sallter', 'jsallter2e@infoseek.co.jp', 'jsallter2e', 'xE2~_RyU2', '1/14/2025', 'suspendido');
insert into lyfter_car_rental.usuarios (id, first_name, last_name, email, username, password, birthdate, state_account) values (88, 'Lurlene', 'Kordes', 'lkordes2f@netvibes.com', 'lkordes2f', 'pV0)taS_N', '6/26/2025', 'inactivo');
insert into lyfter_car_rental.usuarios (id, first_name, last_name, email, username, password, birthdate, state_account) values (89, 'Mirella', 'Middleweek', 'mmiddleweek2g@google.nl', 'mmiddleweek2g', 'sU7''oGJT', '7/6/2024', 'activo');
insert into lyfter_car_rental.usuarios (id, first_name, last_name, email, username, password, birthdate, state_account) values (90, 'Sal', 'Skupinski', 'sskupinski2h@google.pl', 'sskupinski2h', 'wB5*kO5\o>$', '8/9/2026', 'suspendido');
insert into lyfter_car_rental.usuarios (id, first_name, last_name, email, username, password, birthdate, state_account) values (91, 'Simon', 'Meekins', 'smeekins2i@networkadvertising.org', 'smeekins2i', 'kG8_+|,vVA', '6/16/2026', 'suspendido');
insert into lyfter_car_rental.usuarios (id, first_name, last_name, email, username, password, birthdate, state_account) values (92, 'Wren', 'Betts', 'wbetts2j@slideshare.net', 'wbetts2j', 'uM6`*HeFUsov0.', '2/13/2025', 'inactivo');
insert into lyfter_car_rental.usuarios (id, first_name, last_name, email, username, password, birthdate, state_account) values (93, 'Chantal', 'Mannakee', 'cmannakee2k@washingtonpost.com', 'cmannakee2k', 'lH4)6jua9aTea?)', '2/16/2025', 'suspendido');
insert into lyfter_car_rental.usuarios (id, first_name, last_name, email, username, password, birthdate, state_account) values (94, 'Bonnibelle', 'Picheford', 'bpicheford2l@hibu.com', 'bpicheford2l', 'nF3#j''Z0|H>', '3/2/2026', 'inactivo');
insert into lyfter_car_rental.usuarios (id, first_name, last_name, email, username, password, birthdate, state_account) values (95, 'Trixy', 'MacChaell', 'tmacchaell2m@trellian.com', 'tmacchaell2m', 'hY1|_DF<G7N1w98', '12/15/2025', 'suspendido');
insert into lyfter_car_rental.usuarios (id, first_name, last_name, email, username, password, birthdate, state_account) values (96, 'Jermaine', 'Wolseley', 'jwolseley2n@hubpages.com', 'jwolseley2n', 'wG5=d,m!+V''', '5/20/2025', 'inactivo');
insert into lyfter_car_rental.usuarios (id, first_name, last_name, email, username, password, birthdate, state_account) values (97, 'Stanton', 'Poluzzi', 'spoluzzi2o@furl.net', 'spoluzzi2o', 'fJ8}eBw!`', '9/10/2024', 'activo');
insert into lyfter_car_rental.usuarios (id, first_name, last_name, email, username, password, birthdate, state_account) values (98, 'Feliks', 'Bonhome', 'fbonhome2p@army.mil', 'fbonhome2p', 'kH6*sgdFSz', '12/8/2024', 'activo');
insert into lyfter_car_rental.usuarios (id, first_name, last_name, email, username, password, birthdate, state_account) values (99, 'Jabez', 'Broadbear', 'jbroadbear2q@amazon.com', 'jbroadbear2q', 'vD5`FNH%Y!~', '9/11/2024', 'inactivo');
insert into lyfter_car_rental.usuarios (id, first_name, last_name, email, username, password, birthdate, state_account) values (100, 'Rossy', 'Clynter', 'rclynter2r@symantec.com', 'rclynter2r', 'bW0(%L.WiN_h', '8/1/2024', 'inactivo');

select count(*) from lyfter_car_rental.usuarios;
--4. Crear un script para crear la tabla automóviles
DROP TABLE IF EXISTS lyfter_car_rental.automoviles CASCADE;

CREATE TABLE lyfter_car_rental.automoviles(
    id SERIAL PRIMARY KEY,
    make VARCHAR(50) NOT NULL,
    model VARCHAR(50) NOT NULL,
    fabrication_year INTEGER NOT NULL CHECK (fabrication_year BETWEEN 1950 AND EXTRACT(YEAR FROM CURRENT_DATE)),
    state VARCHAR(20) NOT NULL DEFAULT 'disponible' CHECK (state in ('disponible', 'alquilado', 'mantenimiento', 'fuera_de_servicio'))
);

--5 Popular la tabla automóviles
insert into lyfter_car_rental.automoviles (id, make, model, fabrication_year, state) values (1, 'Honda', 'Civic', 1989, 'alquilado');
insert into lyfter_car_rental.automoviles (id, make, model, fabrication_year, state) values (2, 'Isuzu', 'Trooper', 1997, 'mantenimiento');
insert into lyfter_car_rental.automoviles (id, make, model, fabrication_year, state) values (3, 'Chevrolet', 'Tahoe', 1999, 'fuera_de_servicio');
insert into lyfter_car_rental.automoviles (id, make, model, fabrication_year, state) values (4, 'Audi', '5000S', 1988, 'fuera_de_servicio');
insert into lyfter_car_rental.automoviles (id, make, model, fabrication_year, state) values (5, 'Mazda', '323', 1995, 'disponible');
insert into lyfter_car_rental.automoviles (id, make, model, fabrication_year, state) values (6, 'Volvo', 'S40', 2001, 'mantenimiento');
insert into lyfter_car_rental.automoviles (id, make, model, fabrication_year, state) values (7, 'Chevrolet', 'Cavalier', 1995, 'fuera_de_servicio');
insert into lyfter_car_rental.automoviles (id, make, model, fabrication_year, state) values (8, 'Dodge', 'Viper RT/10', 1995, 'mantenimiento');
insert into lyfter_car_rental.automoviles (id, make, model, fabrication_year, state) values (9, 'GMC', 'Savana 3500', 1996, 'alquilado');
insert into lyfter_car_rental.automoviles (id, make, model, fabrication_year, state) values (10, 'Lexus', 'IS F', 2008, 'disponible');
insert into lyfter_car_rental.automoviles (id, make, model, fabrication_year, state) values (11, 'Oldsmobile', 'Aurora', 1996, 'alquilado');
insert into lyfter_car_rental.automoviles (id, make, model, fabrication_year, state) values (12, 'Hyundai', 'Santa Fe', 2003, 'alquilado');
insert into lyfter_car_rental.automoviles (id, make, model, fabrication_year, state) values (13, 'Ford', 'Freestar', 2004, 'disponible');
insert into lyfter_car_rental.automoviles (id, make, model, fabrication_year, state) values (14, 'GMC', 'Rally Wagon 2500', 1992, 'disponible');
insert into lyfter_car_rental.automoviles (id, make, model, fabrication_year, state) values (15, 'Toyota', 'Yaris', 2008, 'fuera_de_servicio');
insert into lyfter_car_rental.automoviles (id, make, model, fabrication_year, state) values (16, 'Nissan', 'NX', 1992, 'mantenimiento');
insert into lyfter_car_rental.automoviles (id, make, model, fabrication_year, state) values (17, 'Land Rover', 'Range Rover', 1994, 'mantenimiento');
insert into lyfter_car_rental.automoviles (id, make, model, fabrication_year, state) values (18, 'Mazda', 'Miata MX-5', 2012, 'mantenimiento');
insert into lyfter_car_rental.automoviles (id, make, model, fabrication_year, state) values (19, 'Suzuki', 'SX4', 2009, 'fuera_de_servicio');
insert into lyfter_car_rental.automoviles (id, make, model, fabrication_year, state) values (20, 'Mazda', 'CX-7', 2010, 'alquilado');
insert into lyfter_car_rental.automoviles (id, make, model, fabrication_year, state) values (21, 'Mitsubishi', 'Montero', 2001, 'fuera_de_servicio');
insert into lyfter_car_rental.automoviles (id, make, model, fabrication_year, state) values (22, 'Acura', 'Integra', 1992, 'mantenimiento');
insert into lyfter_car_rental.automoviles (id, make, model, fabrication_year, state) values (23, 'Mazda', 'Miata MX-5', 2010, 'fuera_de_servicio');
insert into lyfter_car_rental.automoviles (id, make, model, fabrication_year, state) values (24, 'Ford', 'LTD Crown Victoria', 1990, 'alquilado');
insert into lyfter_car_rental.automoviles (id, make, model, fabrication_year, state) values (25, 'Honda', 'Odyssey', 2008, 'alquilado');
insert into lyfter_car_rental.automoviles (id, make, model, fabrication_year, state) values (26, 'Mazda', 'CX-7', 2008, 'disponible');
insert into lyfter_car_rental.automoviles (id, make, model, fabrication_year, state) values (27, 'Lamborghini', 'Gallardo', 2008, 'mantenimiento');
insert into lyfter_car_rental.automoviles (id, make, model, fabrication_year, state) values (28, 'Mercedes-Benz', '500SEL', 1992, 'alquilado');
insert into lyfter_car_rental.automoviles (id, make, model, fabrication_year, state) values (29, 'Toyota', 'Sequoia', 2004, 'mantenimiento');
insert into lyfter_car_rental.automoviles (id, make, model, fabrication_year, state) values (30, 'Lexus', 'GS', 2004, 'mantenimiento');
insert into lyfter_car_rental.automoviles (id, make, model, fabrication_year, state) values (31, 'Chrysler', 'LeBaron', 1993, 'disponible');
insert into lyfter_car_rental.automoviles (id, make, model, fabrication_year, state) values (32, 'Buick', 'Skylark', 1993, 'alquilado');
insert into lyfter_car_rental.automoviles (id, make, model, fabrication_year, state) values (33, 'Toyota', 'Solara', 2003, 'fuera_de_servicio');
insert into lyfter_car_rental.automoviles (id, make, model, fabrication_year, state) values (34, 'GMC', 'Sierra 3500', 2001, 'disponible');
insert into lyfter_car_rental.automoviles (id, make, model, fabrication_year, state) values (35, 'Mercury', 'Monterey', 2007, 'alquilado');
insert into lyfter_car_rental.automoviles (id, make, model, fabrication_year, state) values (36, 'Ford', 'Thunderbird', 1993, 'disponible');
insert into lyfter_car_rental.automoviles (id, make, model, fabrication_year, state) values (37, 'Honda', 'Insight', 2006, 'mantenimiento');
insert into lyfter_car_rental.automoviles (id, make, model, fabrication_year, state) values (38, 'Subaru', 'XT', 1991, 'disponible');
insert into lyfter_car_rental.automoviles (id, make, model, fabrication_year, state) values (39, 'Chevrolet', 'Equinox', 2010, 'mantenimiento');
insert into lyfter_car_rental.automoviles (id, make, model, fabrication_year, state) values (40, 'Audi', 'A8', 2010, 'mantenimiento');
insert into lyfter_car_rental.automoviles (id, make, model, fabrication_year, state) values (41, 'Dodge', 'Ram Van 2500', 1998, 'alquilado');
insert into lyfter_car_rental.automoviles (id, make, model, fabrication_year, state) values (42, 'Nissan', 'Sentra', 2009, 'fuera_de_servicio');
insert into lyfter_car_rental.automoviles (id, make, model, fabrication_year, state) values (43, 'Nissan', 'Murano', 2010, 'alquilado');
insert into lyfter_car_rental.automoviles (id, make, model, fabrication_year, state) values (44, 'Mercury', 'Grand Marquis', 1998, 'fuera_de_servicio');
insert into lyfter_car_rental.automoviles (id, make, model, fabrication_year, state) values (45, 'Audi', '4000CS Quattro', 1987, 'alquilado');
insert into lyfter_car_rental.automoviles (id, make, model, fabrication_year, state) values (46, 'Chevrolet', 'Sportvan G10', 1992, 'alquilado');
insert into lyfter_car_rental.automoviles (id, make, model, fabrication_year, state) values (47, 'Toyota', 'MR2', 1987, 'alquilado');
insert into lyfter_car_rental.automoviles (id, make, model, fabrication_year, state) values (48, 'Lincoln', 'Continental Mark VII', 1985, 'fuera_de_servicio');
insert into lyfter_car_rental.automoviles (id, make, model, fabrication_year, state) values (49, 'Chevrolet', 'Blazer', 1992, 'fuera_de_servicio');
insert into lyfter_car_rental.automoviles (id, make, model, fabrication_year, state) values (50, 'Ford', 'Thunderbird', 1991, 'alquilado');
insert into lyfter_car_rental.automoviles (id, make, model, fabrication_year, state) values (51, 'Pontiac', 'Grand Am', 2002, 'mantenimiento');
insert into lyfter_car_rental.automoviles (id, make, model, fabrication_year, state) values (52, 'Hummer', 'H1', 1997, 'mantenimiento');
insert into lyfter_car_rental.automoviles (id, make, model, fabrication_year, state) values (53, 'Chevrolet', 'Suburban', 2010, 'disponible');
insert into lyfter_car_rental.automoviles (id, make, model, fabrication_year, state) values (54, 'Ford', 'Torino', 1970, 'alquilado');
insert into lyfter_car_rental.automoviles (id, make, model, fabrication_year, state) values (55, 'Lexus', 'LX', 2013, 'mantenimiento');
insert into lyfter_car_rental.automoviles (id, make, model, fabrication_year, state) values (56, 'Dodge', 'Ram Wagon B150', 1992, 'fuera_de_servicio');
insert into lyfter_car_rental.automoviles (id, make, model, fabrication_year, state) values (57, 'Chevrolet', 'Corvette', 2003, 'fuera_de_servicio');
insert into lyfter_car_rental.automoviles (id, make, model, fabrication_year, state) values (58, 'Mitsubishi', 'Mirage', 1999, 'alquilado');
insert into lyfter_car_rental.automoviles (id, make, model, fabrication_year, state) values (59, 'Chevrolet', 'Express 2500', 2010, 'fuera_de_servicio');
insert into lyfter_car_rental.automoviles (id, make, model, fabrication_year, state) values (60, 'Dodge', 'Dakota Club', 2001, 'alquilado');
insert into lyfter_car_rental.automoviles (id, make, model, fabrication_year, state) values (61, 'Mercury', 'Marauder', 2003, 'alquilado');
insert into lyfter_car_rental.automoviles (id, make, model, fabrication_year, state) values (62, 'Dodge', 'Magnum', 2006, 'alquilado');
insert into lyfter_car_rental.automoviles (id, make, model, fabrication_year, state) values (63, 'Dodge', 'Ram Van 2500', 1998, 'disponible');
insert into lyfter_car_rental.automoviles (id, make, model, fabrication_year, state) values (64, 'Ford', 'F-Series', 2004, 'disponible');
insert into lyfter_car_rental.automoviles (id, make, model, fabrication_year, state) values (65, 'Chevrolet', 'Express 2500', 2006, 'fuera_de_servicio');
insert into lyfter_car_rental.automoviles (id, make, model, fabrication_year, state) values (66, 'Nissan', 'Xterra', 2005, 'mantenimiento');
insert into lyfter_car_rental.automoviles (id, make, model, fabrication_year, state) values (67, 'Mitsubishi', 'Montero', 2000, 'disponible');
insert into lyfter_car_rental.automoviles (id, make, model, fabrication_year, state) values (68, 'Ford', 'Crown Victoria', 1996, 'alquilado');
insert into lyfter_car_rental.automoviles (id, make, model, fabrication_year, state) values (69, 'Subaru', 'Legacy', 2010, 'disponible');
insert into lyfter_car_rental.automoviles (id, make, model, fabrication_year, state) values (70, 'Ford', 'F-Series', 1995, 'alquilado');
insert into lyfter_car_rental.automoviles (id, make, model, fabrication_year, state) values (71, 'Toyota', 'RAV4', 1996, 'alquilado');
insert into lyfter_car_rental.automoviles (id, make, model, fabrication_year, state) values (72, 'Lamborghini', 'Murciélago', 2002, 'fuera_de_servicio');
insert into lyfter_car_rental.automoviles (id, make, model, fabrication_year, state) values (73, 'Volkswagen', 'GTI', 2002, 'alquilado');
insert into lyfter_car_rental.automoviles (id, make, model, fabrication_year, state) values (74, 'Mercedes-Benz', 'SL-Class', 2003, 'disponible');
insert into lyfter_car_rental.automoviles (id, make, model, fabrication_year, state) values (75, 'Chevrolet', 'Suburban 1500', 1997, 'alquilado');
insert into lyfter_car_rental.automoviles (id, make, model, fabrication_year, state) values (76, 'Lamborghini', 'Gallardo', 2012, 'alquilado');
insert into lyfter_car_rental.automoviles (id, make, model, fabrication_year, state) values (77, 'GMC', 'Sonoma Club Coupe', 1996, 'disponible');
insert into lyfter_car_rental.automoviles (id, make, model, fabrication_year, state) values (78, 'Acura', 'RL', 2012, 'alquilado');
insert into lyfter_car_rental.automoviles (id, make, model, fabrication_year, state) values (79, 'Ford', 'Escort', 1997, 'alquilado');
insert into lyfter_car_rental.automoviles (id, make, model, fabrication_year, state) values (80, 'Mercedes-Benz', 'CLK-Class', 2008, 'disponible');
insert into lyfter_car_rental.automoviles (id, make, model, fabrication_year, state) values (81, 'GMC', 'Yukon XL 2500', 2000, 'disponible');
insert into lyfter_car_rental.automoviles (id, make, model, fabrication_year, state) values (82, 'Ford', 'E250', 2006, 'mantenimiento');
insert into lyfter_car_rental.automoviles (id, make, model, fabrication_year, state) values (83, 'Chevrolet', 'Astro', 1993, 'alquilado');
insert into lyfter_car_rental.automoviles (id, make, model, fabrication_year, state) values (84, 'Oldsmobile', 'Toronado', 1966, 'mantenimiento');
insert into lyfter_car_rental.automoviles (id, make, model, fabrication_year, state) values (85, 'Chevrolet', 'Corvette', 1984, 'disponible');
insert into lyfter_car_rental.automoviles (id, make, model, fabrication_year, state) values (86, 'Lexus', 'SC', 2010, 'alquilado');
insert into lyfter_car_rental.automoviles (id, make, model, fabrication_year, state) values (87, 'Ford', 'Focus', 2011, 'fuera_de_servicio');
insert into lyfter_car_rental.automoviles (id, make, model, fabrication_year, state) values (88, 'Mercedes-Benz', 'CLK-Class', 1998, 'mantenimiento');
insert into lyfter_car_rental.automoviles (id, make, model, fabrication_year, state) values (89, 'Maserati', 'Quattroporte', 2012, 'fuera_de_servicio');
insert into lyfter_car_rental.automoviles (id, make, model, fabrication_year, state) values (90, 'Chevrolet', 'Camaro', 1975, 'mantenimiento');
insert into lyfter_car_rental.automoviles (id, make, model, fabrication_year, state) values (91, 'Acura', 'Integra', 2001, 'fuera_de_servicio');
insert into lyfter_car_rental.automoviles (id, make, model, fabrication_year, state) values (92, 'Lincoln', 'Town Car', 2010, 'alquilado');
insert into lyfter_car_rental.automoviles (id, make, model, fabrication_year, state) values (93, 'Mercedes-Benz', 'S-Class', 2011, 'alquilado');
insert into lyfter_car_rental.automoviles (id, make, model, fabrication_year, state) values (94, 'GMC', 'Suburban 1500', 1992, 'mantenimiento');
insert into lyfter_car_rental.automoviles (id, make, model, fabrication_year, state) values (95, 'Jeep', 'Wrangler', 2012, 'disponible');
insert into lyfter_car_rental.automoviles (id, make, model, fabrication_year, state) values (96, 'Ford', 'ZX2', 2002, 'mantenimiento');
insert into lyfter_car_rental.automoviles (id, make, model, fabrication_year, state) values (97, 'Chevrolet', 'Malibu', 1997, 'fuera_de_servicio');
insert into lyfter_car_rental.automoviles (id, make, model, fabrication_year, state) values (98, 'Dodge', 'Durango', 2004, 'mantenimiento');
insert into lyfter_car_rental.automoviles (id, make, model, fabrication_year, state) values (99, 'Ford', 'Courier', 1987, 'fuera_de_servicio');
insert into lyfter_car_rental.automoviles (id, make, model, fabrication_year, state) values (100, 'Nissan', '200SX', 1995, 'disponible');

select count(*) from lyfter_car_rental.automoviles;
--6 CREAR LA TABLA CRUZ alquileres
DROP TABLE IF EXISTS lyfter_car_rental.alquiler;

CREATE TABLE lyfter_car_rental.alquiler(
    id SERIAL PRIMARY KEY,
    user_id INTEGER NOT NULL REFERENCES lyfter_car_rental.usuarios(id) ON DELETE CASCADE,
    car_id INTEGER NOT NULL REFERENCES lyfter_car_rental.automoviles(id) ON DELETE CASCADE,
    rental_date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    rental_state VARCHAR(20) NOT NULL DEFAULT 'activo' CHECK (rental_state IN ('activo','finalizado','cancelado'))
);

--7 Popular la tabla cruz
INSERT INTO lyfter_car_rental.alquiler (user_id, car_id, rental_state)
SELECT
    (SELECT id FROM lyfter_car_rental.usuarios ORDER BY random() LIMIT 1)      AS user_id,
    (SELECT id FROM lyfter_car_rental.automoviles ORDER BY random() LIMIT 1)   AS car_id,
    (ARRAY['activo', 'finalizado', 'cancelado'])[floor(random() * 3 + 1)]      AS rental_state
FROM generate_series(1, 150);

select count(*) from lyfter_car_rental.alquiler;