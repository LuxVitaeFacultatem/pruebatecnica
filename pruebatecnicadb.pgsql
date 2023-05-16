--
-- PostgreSQL database dump
--

-- Dumped from database version 15.2
-- Dumped by pg_dump version 15.2

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: Driver; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public."Driver" (
    id integer NOT NULL,
    first_name character varying(30),
    last_name character varying(30),
    mail character varying(40),
    lat_long point,
    creation_date timestamp without time zone,
    status character varying(10)
);


ALTER TABLE public."Driver" OWNER TO postgres;

--
-- Name: TABLE "Driver"; Type: COMMENT; Schema: public; Owner: postgres
--

COMMENT ON TABLE public."Driver" IS 'Driver information table';


--
-- Name: Driver_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public."Driver_id_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public."Driver_id_seq" OWNER TO postgres;

--
-- Name: Driver_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public."Driver_id_seq" OWNED BY public."Driver".id;


--
-- Name: Ride; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public."Ride" (
    id integer NOT NULL,
    rider integer NOT NULL,
    driver integer NOT NULL,
    origin_lat_long point NOT NULL,
    arrive_lat_long point,
    state character varying(9) NOT NULL,
    creation_date timestamp without time zone NOT NULL,
    finish_date timestamp without time zone,
    total_price double precision
);


ALTER TABLE public."Ride" OWNER TO postgres;

--
-- Name: Ride_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public."Ride_id_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public."Ride_id_seq" OWNER TO postgres;

--
-- Name: Ride_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public."Ride_id_seq" OWNED BY public."Ride".id;


--
-- Name: Rider; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public."Rider" (
    id integer NOT NULL,
    first_name character varying(30),
    last_name character varying(30),
    mail character varying(40),
    lat_long point,
    creation_date timestamp without time zone,
    payment_source_id integer
);


ALTER TABLE public."Rider" OWNER TO postgres;

--
-- Name: TABLE "Rider"; Type: COMMENT; Schema: public; Owner: postgres
--

COMMENT ON TABLE public."Rider" IS 'Rider information table';


--
-- Name: Rider_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public."Rider_id_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public."Rider_id_seq" OWNER TO postgres;

--
-- Name: Rider_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public."Rider_id_seq" OWNED BY public."Rider".id;


--
-- Name: Driver id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."Driver" ALTER COLUMN id SET DEFAULT nextval('public."Driver_id_seq"'::regclass);


--
-- Name: Ride id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."Ride" ALTER COLUMN id SET DEFAULT nextval('public."Ride_id_seq"'::regclass);


--
-- Name: Rider id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."Rider" ALTER COLUMN id SET DEFAULT nextval('public."Rider_id_seq"'::regclass);


--
-- Data for Name: Driver; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public."Driver" (id, first_name, last_name, mail, lat_long, creation_date, status) FROM stdin;
1	Adolfo	Ramirez	adolfo@test.com	(3.2530034,-76.5365359)	2016-06-22 19:10:25	available
4	Camilo	Suarez	camilosuarez@test.com	(3.452517851225153,-76.49691843131534)	2022-01-12 12:09:20	available
3	Jhon	Valencia	jhonvalencia@test.com	(3.412613742278438,-76.54111215833122)	2021-02-19 12:09:20	occupied
5	Esneider	Urazan	esneiderurazan@test.com	(3.413407651655433,-76.49019891667731)	2023-04-10 12:09:20	available
2	Alejandro	Quiceno	alejandroquiceno@test.com	(3.4762900227962774,-76.52684105709457)	2020-04-22 14:10:22	available
\.


--
-- Data for Name: Ride; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public."Ride" (id, rider, driver, origin_lat_long, arrive_lat_long, state, creation_date, finish_date, total_price) FROM stdin;
\.


--
-- Data for Name: Rider; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public."Rider" (id, first_name, last_name, mail, lat_long, creation_date, payment_source_id) FROM stdin;
1	Camilo	Ramirez	camilos1900@test.com	(3.344800443402832,-76.5494495444205)	2023-01-12 12:09:20	57153
2	Sofia	Quiceno	sofiaquiceno@test.com	(3.4077723539250826,-76.54267660115678)	2020-04-22 14:10:22	57154
3	Ludin	Villegas	ludinvillegas@test.com	(3.452781936137825,-76.54903383590728)	2016-06-22 19:10:25	57155
4	Carlos	Ramirez	carlosram@test.com	(3.5245943789881835,-76.5252767478134)	2022-01-12 12:09:20	57156
5	Federico	Urazan	piof@test.com	(3.4271501750351803,-76.53691848054552)	2020-02-22 14:10:22	57157
6	Felipe	Sanzz	felipe@test.com	(3.2493016106644177,-76.54767218036095)	2019-02-22 14:10:22	57151
\.


--
-- Name: Driver_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public."Driver_id_seq"', 4, true);


--
-- Name: Ride_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public."Ride_id_seq"', 38, true);


--
-- Name: Rider_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public."Rider_id_seq"', 1, false);


--
-- Name: Driver Driver_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."Driver"
    ADD CONSTRAINT "Driver_pkey" PRIMARY KEY (id);


--
-- Name: Ride Ride_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."Ride"
    ADD CONSTRAINT "Ride_pkey" PRIMARY KEY (id);


--
-- Name: Rider Rider_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."Rider"
    ADD CONSTRAINT "Rider_pkey" PRIMARY KEY (id);


--
-- Name: Ride Driver; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."Ride"
    ADD CONSTRAINT "Driver" FOREIGN KEY (driver) REFERENCES public."Driver"(id);


--
-- Name: Ride Rider; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."Ride"
    ADD CONSTRAINT "Rider" FOREIGN KEY (rider) REFERENCES public."Rider"(id);


--
-- PostgreSQL database dump complete
--

