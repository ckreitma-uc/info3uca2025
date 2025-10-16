import math, time, random

# ------------------- CONFIGURACIÓN -------------------
USE_GLFW = True        # Usa GLFW en tu Mac / GLUT en Mint
WORLD_MIN, WORLD_MAX = -1.0, 1.0
BALL_R      = 0.05
BALL_SPEED  = 0.8
FPS_TARGET  = 60.0
BG_COLOR    = (0.1, 0.1, 0.12, 1.0)
BALL_COLOR  = (1.0, 0.25, 0.25, 1.0)
# -----------------------------------------------------

# ====================== ESTADO ========================
class State:
    def __init__(self):
        self.ball_pos = (0.0, 0.0)
        self.ball_vel = random_velocity()
        self.t_last   = time.perf_counter()

# ===================== UTILIDADES =====================
def random_velocity():
    ang = random.uniform(0, 2*math.pi)
    return (BALL_SPEED * math.cos(ang), BALL_SPEED * math.sin(ang))

def add(a,b): return (a[0]+b[0], a[1]+b[1])
def mul(a,s): return (a[0]*s, a[1]*s)

def update_time(state: State):
    now = time.perf_counter()
    dt  = now - state.t_last
    state.t_last = now
    return dt

# ==================== LÓGICA JUEGO ====================
def move_ball(state: State, dt: float):
    state.ball_pos = add(state.ball_pos, mul(state.ball_vel, dt))

def wall_collision(state: State):
    x, y = state.ball_pos
    vx, vy = state.ball_vel

    if x - BALL_R < WORLD_MIN and vx < 0:
        x = WORLD_MIN + BALL_R
        vx = -vx
    if x + BALL_R > WORLD_MAX and vx > 0:
        x = WORLD_MAX - BALL_R
        vx = -vx
    if y - BALL_R < WORLD_MIN and vy < 0:
        y = WORLD_MIN + BALL_R
        vy = -vy
    if y + BALL_R > WORLD_MAX and vy > 0:
        y = WORLD_MAX - BALL_R
        vy = -vy

    state.ball_pos = (x, y)
    state.ball_vel = (vx, vy)

def update(state: State):
    dt = update_time(state)
    move_ball(state, dt)
    wall_collision(state)

# ===================== DIBUJO =========================
def draw_filled_circle(cx, cy, r, segments=48):
    from OpenGL.GL import glBegin, glEnd, glVertex2f, GL_TRIANGLE_FAN
    glBegin(GL_TRIANGLE_FAN)
    glVertex2f(cx, cy)
    for i in range(segments+1):
        ang = 2*math.pi * i/segments
        glVertex2f(cx + r*math.cos(ang), cy + r*math.sin(ang))
    glEnd()

def render(state: State):
    from OpenGL.GL import (
        glClearColor, glClear, GL_COLOR_BUFFER_BIT,
        glColor4f, glMatrixMode, glLoadIdentity, GL_PROJECTION, GL_MODELVIEW,
        glOrtho
    )
    glClearColor(*BG_COLOR)
    glClear(GL_COLOR_BUFFER_BIT)
    glMatrixMode(GL_PROJECTION); glLoadIdentity()
    glOrtho(WORLD_MIN, WORLD_MAX, WORLD_MIN, WORLD_MAX, -1, 1)
    glMatrixMode(GL_MODELVIEW); glLoadIdentity()
    glColor4f(*BALL_COLOR)
    draw_filled_circle(state.ball_pos[0], state.ball_pos[1], BALL_R)

# ==================== BACKEND GLFW ====================
def run_glfw():
    import glfw
    from OpenGL.GL import glFlush

    if not glfw.init():
        raise SystemExit("GLFW init failed")

    # Contexto 2.1 (modo inmediato)
    glfw.window_hint(glfw.CONTEXT_VERSION_MAJOR, 2)
    glfw.window_hint(glfw.CONTEXT_VERSION_MINOR, 1)
    win = glfw.create_window(800, 800, "Bola Rebota (GLFW)", None, None)
    glfw.make_context_current(win)

    s = State()
    target_dt = 1.0 / FPS_TARGET

    while not glfw.window_should_close(win):
        update(s)
        render(s)
        glFlush()
        glfw.swap_buffers(win)
        glfw.poll_events()
        time.sleep(target_dt)

    glfw.terminate()

# ========================= MAIN =======================
if __name__ == "__main__":
    random.seed()
    if USE_GLFW:
        run_glfw()
    else:
        run_glut()
