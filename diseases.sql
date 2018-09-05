--
-- PostgreSQL database dump
--

-- Dumped from database version 9.5.14
-- Dumped by pg_dump version 9.5.14

-- Started on 2018-09-05 09:55:21 EAT

SET statement_timeout = 0;
SET lock_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_with_oids = false;

--
-- TOC entry 218 (class 1259 OID 29512)
-- Name: farmapp_diseases; Type: TABLE; Schema: public; Owner: xv
--

CREATE TABLE public.farmapp_diseases (
    id integer NOT NULL,
    name text NOT NULL,
    "Image" character varying(100) NOT NULL,
    control text NOT NULL,
    symptoms text NOT NULL
);


ALTER TABLE public.farmapp_diseases OWNER TO xv;

--
-- TOC entry 219 (class 1259 OID 29518)
-- Name: farmapp_diseases_id_seq; Type: SEQUENCE; Schema: public; Owner: xv
--

CREATE SEQUENCE public.farmapp_diseases_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.farmapp_diseases_id_seq OWNER TO xv;

--
-- TOC entry 3613 (class 0 OID 0)
-- Dependencies: 219
-- Name: farmapp_diseases_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: xv
--

ALTER SEQUENCE public.farmapp_diseases_id_seq OWNED BY public.farmapp_diseases.id;


--
-- TOC entry 3482 (class 2604 OID 29578)
-- Name: id; Type: DEFAULT; Schema: public; Owner: xv
--

ALTER TABLE ONLY public.farmapp_diseases ALTER COLUMN id SET DEFAULT nextval('public.farmapp_diseases_id_seq'::regclass);


--
-- TOC entry 3606 (class 0 OID 29512)
-- Dependencies: 218
-- Data for Name: farmapp_diseases; Type: TABLE DATA; Schema: public; Owner: xv
--

COPY public.farmapp_diseases (id, name, "Image", control, symptoms) FROM stdin;
1	Grey leaf Spot	gross/maize_grey_leaf.jpg	Use of tolerant / resistant varieties\r\nGood field sanitation (removal of crop residue after harvest or deep ploughing of crop residues)\r\nUse certified seeds\r\nCrop rotation	They are initially light brownish in colour, and with age they bleach to ashen grey surrounded by narrow light-brownish border. When wet, spore mass is formed on the spots with a light shade.
2	Leaf Blights	gross/maize_blight.jpg	Use of tolerant / resistant varieties\r\nGood field sanitation (removal of crop residue after harvest or deep ploughing of crop residues)\r\nUse certified seeds\r\nCrop rotation	Small yellow dots that become elongated between veins appear. They later become brownish to creamy white in colour with reddish to purplish brown borders. The spots may join together and result in blighting of entire leaves. Silks, portions of the husks and cobs may turn black. A black mould may develop on cobs.
3	Maize Rusts	gross/maize_necrotic.jpg	Use of resistant varieties\r\nCrop rotation\r\nDeep ploughing of crop residue\r\nDestruction of weed Oxalis sp. (an alternate host)	Highland rust produces yellow –brown linear postules on leaves while lowland rust produce light brown postules on upper leave surface.
4	Maize Smut	gross/maize_head_smut.jpg	Use certified seeds\r\nCrop rotation\r\nUse resistant varieties\r\nRogue and destroy by burning the affected plants	The first symptoms become evident when tassels and cobs (ears) appear.\r\nLarge white to black galls on stalks, tassles and ears.\r\nMasses of Black spores are released if galls are opened\r\nThe infested plant to do not produce any grains
5	Maize Streak Virus	gross/maize_streak_virus_tEFzw5s.jpg	Use of tolerant / resistant varieties\r\nEarly rouging\r\nEradication of grass weeds\r\ncontrol vector by spraying with dimethoate, malathion\r\nAvoid overlap of two maize crops\r\nCrop rotation\r\nUse certified maize seed	The virus causes a white to yellowish streaking on the leaves.\r\nThe streaks are very narrow, more or less broken and run parallel along the leaves.\r\nEventually the leaves turn yellow with long lines of green patches\r\nPlants infected at early stage usually do not produce any cobs.\r\nYield losses in East Africa vary between 33 and 55% under natural infection conditions
\.


--
-- TOC entry 3614 (class 0 OID 0)
-- Dependencies: 219
-- Name: farmapp_diseases_id_seq; Type: SEQUENCE SET; Schema: public; Owner: xv
--

SELECT pg_catalog.setval('public.farmapp_diseases_id_seq', 5, true);


--
-- TOC entry 3484 (class 2606 OID 29623)
-- Name: farmapp_diseases_pkey; Type: CONSTRAINT; Schema: public; Owner: xv
--

ALTER TABLE ONLY public.farmapp_diseases
    ADD CONSTRAINT farmapp_diseases_pkey PRIMARY KEY (id);


-- Completed on 2018-09-05 09:55:21 EAT

--
-- PostgreSQL database dump complete
--

