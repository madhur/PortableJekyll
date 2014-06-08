/* -*- Mode: C; tab-width: 8; indent-tabs-mode: t; c-basic-offset: 8; coding: utf-8 -*-
 *  gtksourceview.h
 *
 *  Copyright (C) 2001 - Mikael Hermansson <tyan@linux.se> and
 *  Chris Phelps <chicane@reninet.com>
 *
 *  Copyright (C) 2003 - Gustavo Giráldez and Paolo Maggi
 *
 *  This program is free software; you can redistribute it and/or modify
 *  it under the terms of the GNU Library General Public License as published by
 *  the Free Software Foundation; either version 2 of the License, or
 *  (at your option) any later version.
 *
 *  This program is distributed in the hope that it will be useful,
 *  but WITHOUT ANY WARRANTY; without even the implied warranty of
 *  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 *  GNU Library General Public License for more details.
 *
 *  You should have received a copy of the GNU Library General Public License
 *  along with this program; if not, write to the Free Software
 *  Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA 02111-1307, USA.
 */

#ifndef __GTK_SOURCE_VIEW_H__
#define __GTK_SOURCE_VIEW_H__

#include <gtk/gtk.h>

#include <gtksourceview/gtksourcebuffer.h>
#include <gtksourceview/gtksourcecompletion.h>
#include <gtksourceview/gtksourcegutter.h>

G_BEGIN_DECLS

#define GTK_TYPE_SOURCE_VIEW             (gtk_source_view_get_type ())
#define GTK_SOURCE_VIEW(obj)             (G_TYPE_CHECK_INSTANCE_CAST ((obj), GTK_TYPE_SOURCE_VIEW, GtkSourceView))
#define GTK_SOURCE_VIEW_CLASS(klass)     (G_TYPE_CHECK_CLASS_CAST ((klass), GTK_TYPE_SOURCE_VIEW, GtkSourceViewClass))
#define GTK_IS_SOURCE_VIEW(obj)          (G_TYPE_CHECK_INSTANCE_TYPE ((obj), GTK_TYPE_SOURCE_VIEW))
#define GTK_IS_SOURCE_VIEW_CLASS(klass)  (G_TYPE_CHECK_CLASS_TYPE ((klass), GTK_TYPE_SOURCE_VIEW))
#define GTK_SOURCE_VIEW_GET_CLASS(obj)   (G_TYPE_INSTANCE_GET_CLASS ((obj), GTK_TYPE_SOURCE_VIEW, GtkSourceViewClass))

/**
 * GtkSourceViewGutterPosition:
 * @GTK_SOURCE_VIEW_GUTTER_POSITION_LINES: the gutter position of the lines
 * renderer
 * @GTK_SOURCE_VIEW_GUTTER_POSITION_MARKS: the gutter position of the marks
 * renderer
 **/
typedef enum
{
	GTK_SOURCE_VIEW_GUTTER_POSITION_LINES = -30,
	GTK_SOURCE_VIEW_GUTTER_POSITION_MARKS = -20
} GtkSourceViewGutterPosition;

typedef struct _GtkSourceView GtkSourceView;
typedef struct _GtkSourceViewClass GtkSourceViewClass;

typedef struct _GtkSourceViewPrivate GtkSourceViewPrivate;

struct _GtkSourceView
{
	GtkTextView           parent;

	GtkSourceViewPrivate *priv;
};

struct _GtkSourceViewClass
{
	GtkTextViewClass parent_class;

	void (*undo) (GtkSourceView *view);
	void (*redo) (GtkSourceView *view);
	void (*line_mark_activated) (GtkSourceView *view, 
	                             GtkTextIter   *iter,
	                             GdkEvent      *event);
	void (*show_completion) (GtkSourceView *view);
	void (*move_lines) (GtkSourceView *view,
	                    gboolean       copy,
	                    gint           step);

	/* Padding for future expansion */
	void (*_gtk_source_reserved1) (void);
};

/**
 * GtkSourceSmartHomeEndType:
 * @GTK_SOURCE_SMART_HOME_END_DISABLED: smart-home-end disabled.
 * @GTK_SOURCE_SMART_HOME_END_BEFORE: move to the first/last
 * non-whitespace character on the first press of the HOME/END keys and
 * to the beginning/end of the line on the second press.
 * @GTK_SOURCE_SMART_HOME_END_AFTER: move to the beginning/end of the
 * line on the first press of the HOME/END keys and to the first/last
 * non-whitespace character on the second press.
 * @GTK_SOURCE_SMART_HOME_END_ALWAYS: always move to the first/last
 * non-whitespace character when the HOME/END keys are pressed.
 **/
typedef enum
{
	GTK_SOURCE_SMART_HOME_END_DISABLED,
	GTK_SOURCE_SMART_HOME_END_BEFORE,
	GTK_SOURCE_SMART_HOME_END_AFTER,
	GTK_SOURCE_SMART_HOME_END_ALWAYS
} GtkSourceSmartHomeEndType;

/**
 * GtkSourceDrawSpacesFlags:
 * @GTK_SOURCE_DRAW_SPACES_SPACE: whether the space character should be drawn.
 * @GTK_SOURCE_DRAW_SPACES_TAB: whether the tab character should be drawn.
 * @GTK_SOURCE_DRAW_SPACES_NEWLINE: whether the line breaks should be drawn.
 * @GTK_SOURCE_DRAW_SPACES_NBSP: whether the non-breaking whitespaces should be drawn.
 * @GTK_SOURCE_DRAW_SPACES_ALL: wheter all kind of spaces should be drawn.
 *
 * GtkSourceDrawSpacesFlags determine what kind of spaces whould be drawn.
 */
typedef enum
{
	GTK_SOURCE_DRAW_SPACES_SPACE      = 1 << 0,
	GTK_SOURCE_DRAW_SPACES_TAB        = 1 << 1,
	GTK_SOURCE_DRAW_SPACES_NEWLINE    = 1 << 2,
	GTK_SOURCE_DRAW_SPACES_NBSP       = 1 << 3,
	GTK_SOURCE_DRAW_SPACES_LEADING    = 1 << 4,
	GTK_SOURCE_DRAW_SPACES_TEXT       = 1 << 5,
	GTK_SOURCE_DRAW_SPACES_TRAILING   = 1 << 6,
	GTK_SOURCE_DRAW_SPACES_ALL        = (GTK_SOURCE_DRAW_SPACES_SPACE   | \
	                                     GTK_SOURCE_DRAW_SPACES_TAB     | \
	                                     GTK_SOURCE_DRAW_SPACES_NEWLINE | \
	                                     GTK_SOURCE_DRAW_SPACES_NBSP | \
	                                     GTK_SOURCE_DRAW_SPACES_LEADING | \
	                                     GTK_SOURCE_DRAW_SPACES_TEXT | \
	                                     GTK_SOURCE_DRAW_SPACES_TRAILING)
} GtkSourceDrawSpacesFlags;


GType		 gtk_source_view_get_type 		(void) G_GNUC_CONST;

/* Constructors */
GtkWidget 	*gtk_source_view_new 			(void);
GtkWidget 	*gtk_source_view_new_with_buffer	(GtkSourceBuffer *buffer);

/* Properties */
void 		 gtk_source_view_set_show_line_numbers 	(GtkSourceView   *view,
							 gboolean         show);
gboolean 	 gtk_source_view_get_show_line_numbers 	(GtkSourceView   *view);

void 		 gtk_source_view_set_tab_width          (GtkSourceView   *view,
							 guint            width);
guint            gtk_source_view_get_tab_width          (GtkSourceView   *view);

void		 gtk_source_view_set_indent_width 	(GtkSourceView   *view,
							 gint             width);
gint		 gtk_source_view_get_indent_width	(GtkSourceView   *view);

void		 gtk_source_view_set_auto_indent 	(GtkSourceView   *view,
							 gboolean         enable);
gboolean	 gtk_source_view_get_auto_indent 	(GtkSourceView   *view);

void		 gtk_source_view_set_insert_spaces_instead_of_tabs
							(GtkSourceView   *view,
							 gboolean         enable);
gboolean	 gtk_source_view_get_insert_spaces_instead_of_tabs
							(GtkSourceView   *view);

void		 gtk_source_view_set_indent_on_tab 	(GtkSourceView   *view,
							 gboolean         enable);
gboolean	 gtk_source_view_get_indent_on_tab 	(GtkSourceView   *view);

void		 gtk_source_view_set_highlight_current_line
							(GtkSourceView   *view,
							 gboolean         show);
gboolean 	 gtk_source_view_get_highlight_current_line
							(GtkSourceView   *view);

void		 gtk_source_view_set_show_right_margin 	(GtkSourceView   *view,
							 gboolean         show);
gboolean 	 gtk_source_view_get_show_right_margin 	(GtkSourceView   *view);

void		 gtk_source_view_set_right_margin_position
					 		(GtkSourceView   *view,
							 guint            pos);
guint		 gtk_source_view_get_right_margin_position
					 		(GtkSourceView   *view);

void 		 gtk_source_view_set_show_line_marks    (GtkSourceView   *view,
							 gboolean         show);
gboolean	 gtk_source_view_get_show_line_marks    (GtkSourceView   *view);

#ifndef GTKSOURCEVIEW_DISABLE_DEPRECATED
void		 gtk_source_view_set_mark_category_pixbuf
							(GtkSourceView   *view,
							const gchar      *category,
							GdkPixbuf        *pixbuf) G_GNUC_DEPRECATED;
#endif

void             gtk_source_view_set_mark_category_icon_from_pixbuf
							(GtkSourceView   *view,
							 const gchar     *category,
							 GdkPixbuf       *pixbuf);

void             gtk_source_view_set_mark_category_icon_from_stock
							(GtkSourceView   *view,
							 const gchar     *category,
							 const gchar     *stock_id);

void             gtk_source_view_set_mark_category_icon_from_icon_name
							(GtkSourceView   *view,
							 const gchar     *category,
							 const gchar     *name);

#ifndef GTKSOURCEVIEW_DISABLE_DEPRECATED
GdkPixbuf	*gtk_source_view_get_mark_category_pixbuf
							(GtkSourceView   *view,
				       			 const gchar     *category) G_GNUC_DEPRECATED;
#endif

void             gtk_source_view_set_mark_category_background
							(GtkSourceView   *view,
							 const gchar     *category,
							 const GdkColor  *color);
gboolean         gtk_source_view_get_mark_category_background
							(GtkSourceView   *view,
							 const gchar     *category,
							 GdkColor        *dest);

/**
 * GtkSourceViewMarkTooltipFunc:
 * @mark: the #GtkSourceMark
 * @user_data: user data pointer which was passed to gtk_source_view_set_mark_category_tooltip_func()
 *
 * Function type for setting up a tooltip for #GtkSourceMark.
 * Returns: a newly-allocated string that is going to be shown as tooltip text.
 */
typedef gchar *  (*GtkSourceViewMarkTooltipFunc)	(GtkSourceMark	*mark,
							 gpointer	 user_data);
void             gtk_source_view_set_mark_category_tooltip_func
							(GtkSourceView   *view,
							 const gchar     *category,
							 GtkSourceViewMarkTooltipFunc func,
							 gpointer	  user_data,
							 GDestroyNotify   user_data_notify);
void		 gtk_source_view_set_mark_category_tooltip_markup_func
							(GtkSourceView   *view,
							const gchar     *category,
							GtkSourceViewMarkTooltipFunc markup_func,
							gpointer         user_data,
							GDestroyNotify   user_data_notify);

void             gtk_source_view_set_mark_category_priority
							(GtkSourceView   *view,
							 const gchar     *category,
							 gint priority);
gint		 gtk_source_view_get_mark_category_priority
							(GtkSourceView   *view,
				       			 const gchar     *category);

void		 gtk_source_view_set_smart_home_end	(GtkSourceView             *view,
							 GtkSourceSmartHomeEndType  smart_he);
GtkSourceSmartHomeEndType
		 gtk_source_view_get_smart_home_end	(GtkSourceView   *view);

void		 gtk_source_view_set_draw_spaces	(GtkSourceView   *view,
							 GtkSourceDrawSpacesFlags flags);
GtkSourceDrawSpacesFlags
		gtk_source_view_get_draw_spaces		(GtkSourceView   *view);

GtkSourceCompletion *
		gtk_source_view_get_completion		(GtkSourceView   *view);

GtkSourceGutter *gtk_source_view_get_gutter		(GtkSourceView     *view,
                                                         GtkTextWindowType  window_type);

G_END_DECLS
#endif				/* end of SOURCE_VIEW_H__ */
