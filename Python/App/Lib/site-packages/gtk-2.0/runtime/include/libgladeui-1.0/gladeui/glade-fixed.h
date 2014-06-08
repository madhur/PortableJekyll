/* -*- Mode: C; tab-width: 8; indent-tabs-mode: t; c-basic-offset: 8 -*- */
#ifndef __GLADE_FIXED_H__
#define __GLADE_FIXED_H__

#include <glib-object.h>
#include <gdk/gdk.h>

#include <gladeui/glade-widget.h>
#include <gladeui/glade-cursor.h>

G_BEGIN_DECLS

#define GLADE_TYPE_FIXED            (glade_fixed_get_type())
#define GLADE_FIXED(obj)            (G_TYPE_CHECK_INSTANCE_CAST ((obj), GLADE_TYPE_FIXED, GladeFixed))
#define GLADE_FIXED_CLASS(klass)    (G_TYPE_CHECK_CLASS_CAST ((klass), GLADE_TYPE_FIXED, GladeFixedClass))
#define GLADE_IS_FIXED(obj)         (G_TYPE_CHECK_INSTANCE_TYPE ((obj), GLADE_TYPE_FIXED))
#define GLADE_IS_FIXED_CLASS(klass) (G_TYPE_CHECK_CLASS_TYPE ((klass), GLADE_TYPE_FIXED))
#define GLADE_FIXED_GET_CLASS(o)    (G_TYPE_INSTANCE_GET_CLASS ((o), GLADE_FIXED, GladeFixedClass))

/* Convenience macros used in pointer events.
 */
#define GLADE_FIXED_CURSOR_TOP(type)                      \
	((type) == GLADE_CURSOR_RESIZE_TOP_RIGHT ||       \
	 (type) == GLADE_CURSOR_RESIZE_TOP_LEFT  ||       \
	 (type) == GLADE_CURSOR_RESIZE_TOP)

#define GLADE_FIXED_CURSOR_BOTTOM(type)                   \
	((type) == GLADE_CURSOR_RESIZE_BOTTOM_RIGHT ||    \
	 (type) == GLADE_CURSOR_RESIZE_BOTTOM_LEFT  ||    \
	 (type) == GLADE_CURSOR_RESIZE_BOTTOM)

#define GLADE_FIXED_CURSOR_RIGHT(type)                    \
	((type) == GLADE_CURSOR_RESIZE_TOP_RIGHT    ||    \
	 (type) == GLADE_CURSOR_RESIZE_BOTTOM_RIGHT ||    \
	 (type) == GLADE_CURSOR_RESIZE_RIGHT)

#define GLADE_FIXED_CURSOR_LEFT(type)                    \
	((type) == GLADE_CURSOR_RESIZE_TOP_LEFT    ||    \
	 (type) == GLADE_CURSOR_RESIZE_BOTTOM_LEFT ||    \
	 (type) == GLADE_CURSOR_RESIZE_LEFT)

typedef struct _GladeFixed        GladeFixed;
typedef struct _GladeFixedClass   GladeFixedClass;

struct _GladeFixed {
	GladeWidget       parent_instance;

	gchar            *x_prop;      /* packing property names (on child widgets) used */
	gchar            *y_prop;      /* to obtain & configure widget coordinates */
	gchar            *width_prop;  /* property names (on child widgets) used to obtain */
	gchar            *height_prop; /* & configure widget dimentions. */

        gboolean          can_resize; /* whether the container supports child resizes or only
				       * drags.
				       */

	/* State machine used to commit properties at the end
	 * of a drag or a resize (i.e. a "configure").
	 */
	gint              pointer_x_origin;
	gint              pointer_y_origin;
	gint              pointer_x_child_origin;
	gint              pointer_y_child_origin;
	gint              child_x_origin;
	gint              child_y_origin;
	gint              child_width_origin;
	gint              child_height_origin;

	GladeWidget      *configuring;
	GladeCursorType   operation;
	gboolean          creating;
	gint              mouse_x;
	gint              mouse_y;
};

struct _GladeFixedClass {
	GladeWidgetClass   parent_class;

	gboolean     (* configure_child) (GladeFixed *, GladeWidget *, GdkRectangle *);
	gboolean     (* configure_begin) (GladeFixed *, GladeWidget *);
	gboolean     (* configure_end)   (GladeFixed *, GladeWidget *);

	/* Signal handler for child widgets
	 */
	gint         (* child_event)     (GladeWidget *, GdkEvent *, GladeFixed *);

};

GType              glade_fixed_get_type     (void);

G_END_DECLS

#endif   /* __GLADE_FIXED_H__ */
