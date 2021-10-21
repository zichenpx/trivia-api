--
-- PostgreSQL database dump
--

-- Dumped from database version 13.2
-- Dumped by pg_dump version 13.2

-- Started on 2021-09-30 21:07:04

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
-- TOC entry 204 (class 1259 OID 57534)
-- Name: alembic_version; Type: TABLE; Schema: public; Owner: USER
--

CREATE TABLE public.alembic_version (
    version_num character varying(32) NOT NULL
);


ALTER TABLE public.alembic_version OWNER TO "USER";

--
-- TOC entry 200 (class 1259 OID 57502)
-- Name: categories; Type: TABLE; Schema: public; Owner: USER
--

CREATE TABLE public.categories (
    id integer NOT NULL,
    type text
);


ALTER TABLE public.categories OWNER TO "USER";

--
-- TOC entry 201 (class 1259 OID 57508)
-- Name: categories_id_seq; Type: SEQUENCE; Schema: public; Owner: USER
--

CREATE SEQUENCE public.categories_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.categories_id_seq OWNER TO "USER";

--
-- TOC entry 3010 (class 0 OID 0)
-- Dependencies: 201
-- Name: categories_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: USER
--

ALTER SEQUENCE public.categories_id_seq OWNED BY public.categories.id;


--
-- TOC entry 202 (class 1259 OID 57510)
-- Name: questions; Type: TABLE; Schema: public; Owner: USER
--

CREATE TABLE public.questions (
    id integer NOT NULL,
    question text,
    answer text,
    difficulty integer,
    category integer,
    creator character varying
);


ALTER TABLE public.questions OWNER TO "USER";

--
-- TOC entry 203 (class 1259 OID 57516)
-- Name: questions_id_seq; Type: SEQUENCE; Schema: public; Owner: USER
--

CREATE SEQUENCE public.questions_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.questions_id_seq OWNER TO "USER";

--
-- TOC entry 3011 (class 0 OID 0)
-- Dependencies: 203
-- Name: questions_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: USER
--

ALTER SEQUENCE public.questions_id_seq OWNED BY public.questions.id;


--
-- TOC entry 2862 (class 2604 OID 57518)
-- Name: categories id; Type: DEFAULT; Schema: public; Owner: USER
--

ALTER TABLE ONLY public.categories ALTER COLUMN id SET DEFAULT nextval('public.categories_id_seq'::regclass);


--
-- TOC entry 2863 (class 2604 OID 57519)
-- Name: questions id; Type: DEFAULT; Schema: public; Owner: USER
--

ALTER TABLE ONLY public.questions ALTER COLUMN id SET DEFAULT nextval('public.questions_id_seq'::regclass);


--
-- TOC entry 3004 (class 0 OID 57534)
-- Dependencies: 204
-- Data for Name: alembic_version; Type: TABLE DATA; Schema: public; Owner: USER
--

COPY public.alembic_version (version_num) FROM stdin;
9ca626d7ba9a
\.


--
-- TOC entry 3000 (class 0 OID 57502)
-- Dependencies: 200
-- Data for Name: categories; Type: TABLE DATA; Schema: public; Owner: USER
--

COPY public.categories (id, type) FROM stdin;
1	Science
2	Art
3	Geography
4	History
5	Entertainment
6	Sports
7	Food
8	Cosmetics
\.


--
-- TOC entry 3002 (class 0 OID 57510)
-- Dependencies: 202
-- Data for Name: questions; Type: TABLE DATA; Schema: public; Owner: USER
--

COPY public.questions (id, question, answer, difficulty, category, creator) FROM stdin;
1	Biggest organ in human body?	Skin	3	1	Max
5	Whose autobiography is entitled 'I Know Why the Caged Bird Sings'?	Maya Angelou	2	4	Emily
9	What boxer's original name is Cassius Clay?	Muhammad Ali	1	4	Sylvia
2	What movie earned Tom Hanks his third straight Oscar nomination, in 1996?	Apollo 13	4	5	Sylvia
4	What actor did author Anne Rice first denounce, then praise in the role of her beloved Lestat?	Tom Cruise	4	5	Sylvia
6	What was the title of the 1990 fantasy directed by Tim Burton about a young man with multi-bladed appendages?	Edward Scissorhands	3	5	Sylvia
10	Which is the only team to play in every soccer World Cup tournament?	Brazil	3	6	Emily
11	Which country won the first ever soccer World Cup in 1930?	Uruguay	4	6	Max
12	Who invented Peanut Butter?	George Washington Carver	2	4	Emily
13	What is the largest lake in Africa?	Lake Victoria	2	3	Emily
14	In which royal palace would you find the Hall of Mirrors?	The Palace of Versailles	3	3	Max
15	The Taj Mahal is located in which Indian city?	Agra	2	3	Emily
16	Which Dutch graphic artist–initials M C was a creator of optical illusions?	Escher	1	2	Sylvia
17	La Giaconda is better known as what?	Mona Lisa	3	2	Argy
18	How many paintings did Van Gogh sell in his lifetime?	One	4	2	Max
19	Which American artist was a pioneer of Abstract Expressionism, and a leading exponent of action painting?	Jackson Pollock	2	2	Argy
20	What is the heaviest organ in the human body?	The Liver	4	1	Argy
21	Who discovered penicillin?	Alexander Fleming	3	1	Argy
22	Hematology is a branch of medicine involving the study of what?	Blood	4	1	Argy
23	Which dung beetle was worshipped by the ancient Egyptians?	Scarab	4	4	Max
24	The capital of Taiwan(ROC)	Taipei	2	3	Amy
\.


--
-- TOC entry 3012 (class 0 OID 0)
-- Dependencies: 201
-- Name: categories_id_seq; Type: SEQUENCE SET; Schema: public; Owner: USER
--

SELECT pg_catalog.setval('public.categories_id_seq', 8, true);


--
-- TOC entry 3013 (class 0 OID 0)
-- Dependencies: 203
-- Name: questions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: USER
--

SELECT pg_catalog.setval('public.questions_id_seq', 24, true);


--
-- TOC entry 2869 (class 2606 OID 57538)
-- Name: alembic_version alembic_version_pkc; Type: CONSTRAINT; Schema: public; Owner: USER
--

ALTER TABLE ONLY public.alembic_version
    ADD CONSTRAINT alembic_version_pkc PRIMARY KEY (version_num);


--
-- TOC entry 2865 (class 2606 OID 57521)
-- Name: categories categories_pkey; Type: CONSTRAINT; Schema: public; Owner: USER
--

ALTER TABLE ONLY public.categories
    ADD CONSTRAINT categories_pkey PRIMARY KEY (id);


--
-- TOC entry 2867 (class 2606 OID 57523)
-- Name: questions questions_pkey; Type: CONSTRAINT; Schema: public; Owner: USER
--

ALTER TABLE ONLY public.questions
    ADD CONSTRAINT questions_pkey PRIMARY KEY (id);


-- Completed on 2021-09-30 21:07:04

--
-- PostgreSQL database dump complete
--

