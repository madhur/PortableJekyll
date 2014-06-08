/* -*- Mode: C; tab-width: 8; indent-tabs-mode: t; c-basic-offset: 8 -*- */
/* TODO : s/glade_xml_get_/glade_xml_node_get/g */
#ifndef __GLADE_XML_UTILS_H__
#define __GLADE_XML_UTILS_H__

#include <glib.h>
#include <gmodule.h>


G_BEGIN_DECLS

#define GLADE_XML_CONTEXT(c)    ((GladeXmlContext *)c)
#define GLADE_XML_IS_CONTEXT(c) (c != NULL)

#define CAST_BAD (gchar *)


typedef struct _GladeXmlContext GladeXmlContext;
typedef struct _GladeXmlNode    GladeXmlNode;
typedef struct _GladeXmlDoc     GladeXmlDoc;

/* FIXME: forward declarations to get around circular header dependencies.
 */
typedef struct _GladeWidget    GladeWidget;
typedef struct _GladeProperty  GladeProperty;
typedef struct _GladeProject   GladeProject;


/* We define this here only because our headers need
 * a good sorting
 */
typedef enum
{
	GLADE_PROJECT_FORMAT_LIBGLADE,
	GLADE_PROJECT_FORMAT_GTKBUILDER
} GladeProjectFormat;


typedef enum {
	GLADE_POLICY_PROJECT_WIDE = 0,    /* widget names are unique throughout the project */
	GLADE_POLICY_TOPLEVEL_CONTEXTUAL  /* toplevel names are unique, and widgets inside a toplevel */
} GladeNamingPolicy;


#define GLADE_XML_TAG_PROJECT(type) \
	((type == GLADE_PROJECT_FORMAT_LIBGLADE) ? \
	 GLADE_XML_TAG_LIBGLADE_PROJECT : GLADE_XML_TAG_BUILDER_PROJECT)

#define GLADE_XML_TAG_WIDGET(type) \
	((type == GLADE_PROJECT_FORMAT_LIBGLADE) ? \
	 GLADE_XML_TAG_LIBGLADE_WIDGET : GLADE_XML_TAG_BUILDER_WIDGET)

#define GLADE_GTKBUILDER_VERSIONING_BASE_MAJOR    2
#define GLADE_GTKBUILDER_VERSIONING_BASE_MINOR    14
#define GLADE_GTKBUILDER_HAS_VERSIONING(maj, min) \
	((maj) >= GLADE_GTKBUILDER_VERSIONING_BASE_MAJOR && \
	 (min) >= GLADE_GTKBUILDER_VERSIONING_BASE_MINOR)


/* Used for catalog tags and attributes */
#define GLADE_XML_TAG_LIBGLADE_PROJECT            "glade-interface"
#define GLADE_XML_TAG_BUILDER_PROJECT             "interface"
#define GLADE_XML_TAG_LIBGLADE_WIDGET             "widget"
#define GLADE_XML_TAG_BUILDER_WIDGET              "object"

#define GLADE_XML_TAG_VERSION                     "version"
#define GLADE_XML_TAG_REQUIRES                    "requires"
#define GLADE_XML_TAG_LIB                         "lib"
#define GLADE_XML_TAG_PROPERTY                    "property"
#define GLADE_XML_TAG_CLASS                       "class"
#define GLADE_XML_TAG_ID                          "id"
#define GLADE_XML_TAG_SIGNAL                      "signal"
#define GLADE_XML_TAG_HANDLER                     "handler"
#define GLADE_XML_TAG_AFTER                       "after"
#define GLADE_XML_TAG_SWAPPED                     "swapped"
#define GLADE_XML_TAG_OBJECT                      "object"
#define GLADE_XML_TAG_NAME                        "name"
#define GLADE_XML_TAG_CHILD                       "child"
#define GLADE_XML_TAG_PACKING                     "packing"
#define GLADE_XML_TAG_PLACEHOLDER                 "placeholder"
#define GLADE_XML_TAG_INTERNAL_CHILD              "internal-child"
#define GLADE_XML_TAG_I18N_TRUE                   "yes"
#define GLADE_XML_TAG_SIGNAL_TRUE                 "yes"
#define GLADE_XML_TAG_SIGNAL_FALSE                "no"
#define GLADE_XML_TAG_TYPE                        "type"
#define GLADE_XML_TAG_SOURCES                     "sources"
#define GLADE_XML_TAG_SOURCE                      "source"
#define GLADE_XML_TAG_FILENAME                    "filename"
#define GLADE_XML_TAG_STOCK_ID                    "stock-id"

#define GLADE_TAG_VERSION                         "version"
#define GLADE_TAG_TARGETABLE                      "targetable"
#define GLADE_TAG_VERSION_SINCE                   "since"
#define GLADE_TAG_BUILDER_SINCE                   "gtkbuilder-since"
#define GLADE_TAG_DEPRECATED                      "deprecated"

#define GLADE_TAG_LIBGLADE_ONLY                   "libglade-only"
#define GLADE_TAG_LIBGLADE_UNSUPPORTED            "libglade-unsupported"
#define GLADE_TAG_SUPPORTS                        "supports"
#define GLADE_TAG_GTKBUILDER                      "gtkbuilder"
#define GLADE_TAG_LIBGLADE                        "libglade"

#define GLADE_TAG_GLADE_CATALOG                   "glade-catalog"
#define GLADE_TAG_GLADE_WIDGET_CLASSES            "glade-widget-classes"
#define GLADE_TAG_GLADE_WIDGET_CLASS              "glade-widget-class"
#define GLADE_TAG_GLADE_WIDGET_GROUP              "glade-widget-group"
#define GLADE_TAG_GLADE_WIDGET_CLASS_REF          "glade-widget-class-ref"
#define GLADE_TAG_ADAPTOR                         "adaptor"
#define GLADE_TAG_LIBRARY                         "library"
#define GLADE_TAG_DEPENDS                         "depends"
#define GLADE_TAG_DOMAIN                          "domain"
#define GLADE_TAG_BOOK                            "book"
#define GLADE_TAG_SIGNALS                         "signals"
#define GLADE_TAG_SIGNAL                          "signal"
#define GLADE_TAG_DEFAULT                         "default"
#define GLADE_TAG_PARENTLESS_WIDGET               "parentless-widget"
#define GLADE_TAG_DISABLED                        "disabled"
#define GLADE_TAG_CONSTRUCT_ONLY                  "construct-only"
#define GLADE_TAG_NEEDS_SYNC                      "needs-sync"
#define GLADE_TAG_DEFAULT_PALETTE_STATE           "default-palette-state"
#define GLADE_TAG_PROJECT_CONVERT_FUNCTION        "project-convert-function"
#define GLADE_TAG_REPLACE_CHILD_FUNCTION          "replace-child-function"
#define GLADE_TAG_CONSTRUCT_OBJECT_FUNCTION       "construct-object-function"
#define GLADE_TAG_DEEP_POST_CREATE_FUNCTION       "deep-post-create-function"
#define GLADE_TAG_POST_CREATE_FUNCTION            "post-create-function"
#define GLADE_TAG_GET_INTERNAL_CHILD_FUNCTION     "get-internal-child-function"
#define GLADE_TAG_ADD_CHILD_FUNCTION              "add-child-function"
#define GLADE_TAG_REMOVE_CHILD_FUNCTION           "remove-child-function"
#define GLADE_TAG_GET_CHILDREN_FUNCTION           "get-children-function"
#define GLADE_TAG_CHILD_SET_PROP_FUNCTION         "child-set-property-function"
#define GLADE_TAG_CHILD_GET_PROP_FUNCTION         "child-get-property-function"
#define GLADE_TAG_CHILD_VERIFY_FUNCTION           "child-verify-function"
#define GLADE_TAG_CONSTRUCTOR_FUNCTION            "constructor-function"
#define GLADE_TAG_ACTION_ACTIVATE_FUNCTION        "action-activate-function"
#define GLADE_TAG_CHILD_ACTION_ACTIVATE_FUNCTION  "child-action-activate-function"
#define GLADE_TAG_ACTION_SUBMENU_FUNCTION         "action-submenu-function"
#define GLADE_TAG_DEPENDS_FUNCTION                "depends-function"
#define GLADE_TAG_READ_WIDGET_FUNCTION            "read-widget-function"
#define GLADE_TAG_WRITE_WIDGET_FUNCTION           "write-widget-function"
#define GLADE_TAG_READ_CHILD_FUNCTION             "read-child-function"
#define GLADE_TAG_WRITE_CHILD_FUNCTION            "write-child-function"
#define GLADE_TAG_CREATE_EPROP_FUNCTION           "create-editor-property-function"
#define GLADE_TAG_STRING_FROM_VALUE_FUNCTION      "string-from-value-function"
#define GLADE_TAG_CREATE_EDITABLE_FUNCTION        "create-editable-function"
#define GLADE_TAG_PROPERTIES                      "properties"
#define GLADE_TAG_PACKING_PROPERTIES              "packing-properties"
#define GLADE_TAG_PROPERTY                        "property"
#define GLADE_TAG_ACTIONS                         "actions"
#define GLADE_TAG_PACKING_ACTIONS                 "packing-actions"
#define GLADE_TAG_ACTION                          "action"
#define GLADE_TAG_TYPE                            "type"
#define GLADE_TAG_SPEC                            "spec"
#define GLADE_TAG_SPECIFICATIONS                  "parameter-spec"
#define GLADE_TAG_MAX_VALUE                       "max"
#define GLADE_TAG_MIN_VALUE                       "min"
#define GLADE_TAG_VALUE_TYPE                      "value-type"
#define GLADE_TAG_TOOLTIP                         "tooltip"
#define GLADE_TAG_PARAMETERS                      "parameters"
#define GLADE_TAG_PARAMETER                       "parameter"
#define GLADE_TAG_SET_FUNCTION                    "set-property-function"
#define GLADE_TAG_GET_FUNCTION                    "get-property-function"
#define GLADE_TAG_VERIFY_FUNCTION                 "verify-function"
#define GLADE_TAG_QUERY                           "query"
#define GLADE_TAG_COMMON                          "common"
#define GLADE_TAG_OPTIONAL                        "optional"
#define GLADE_TAG_OPTIONAL_DEFAULT                "optional-default"
#define GLADE_TAG_VISIBLE                         "visible"
#define GLADE_TAG_CUSTOM_LAYOUT                   "custom-layout"
#define GLADE_TAG_EXPANDED                        "expanded"
#define GLADE_TAG_GENERIC_NAME                    "generic-name"
#define GLADE_TAG_NAME                            "name"
#define GLADE_TAG_PARENT                          "parent"
#define GLADE_TAG_TITLE                           "title"
#define GLADE_TAG_ID                              "id"
#define GLADE_TAG_KEY                             "key"
#define GLADE_TAG_VALUE                           "value"
#define GLADE_TAG_TRANSLATABLE                    "translatable"
#define GLADE_TAG_HAS_CONTEXT                     "context"
#define GLADE_TAG_CONTEXT                         "context"
#define GLADE_TAG_COMMENT                         "comments"
#define GLADE_TAG_PACKING_DEFAULTS                "packing-defaults"
#define GLADE_TAG_PARENT_CLASS                    "parent-class"
#define GLADE_TAG_CHILD_PROPERTY                  "child-property"
#define GLADE_TAG_DISPLAYABLE_VALUES              "displayable-values"
#define GLADE_TAG_NICK                            "nick"
#define GLADE_TAG_SPECIAL_CHILD_TYPE              "special-child-type"
#define GLADE_TAG_SAVE                            "save"
#define GLADE_TAG_SAVE_ALWAYS                     "save-always"
#define GLADE_TAG_EDITABLE                        "editable"
#define GLADE_TAG_IGNORE                          "ignore"
#define GLADE_TAG_VISIBLE_LINES                   "visible-lines"
#define GLADE_TAG_RESOURCE                        "resource"
#define GLADE_TAG_STOCK                           "stock"
#define GLADE_TAG_STOCK_ICON                      "stock-icon"
#define GLADE_TAG_THEMED_ICON                     "themed-icon"
#define GLADE_TAG_INIT_FUNCTION                   "init-function"
#define GLADE_TAG_ATK_PROPERTY                    "atk-property"
#define GLADE_TAG_FIXED                           "fixed"
#define GLADE_TAG_TRANSFER_ON_PASTE               "transfer-on-paste"
#define GLADE_TAG_WEIGHT                          "weight"
#define GLADE_TAG_GET_TYPE_FUNCTION               "get-type-function"
#define GLADE_TAG_TOPLEVEL                        "toplevel"
#define GLADE_TAG_USE_PLACEHOLDERS                "use-placeholders"
#define GLADE_TAG_DEFAULT_WIDTH                   "default-width"
#define GLADE_TAG_DEFAULT_HEIGHT                  "default-height"
#define GLADE_TAG_EVENT_HANDLER_CONNECTED         "EventHandlerConnected"
#define GLADE_TAG_FALSE                           "False"
#define GLADE_TAG_TRUE                            "True"
#define GLADE_TAG_YES                             "Yes"
#define GLADE_TAG_NO                              "No"
#define GLADE_TAG_ICON_PREFIX                     "icon-prefix"
#define GLADE_TAG_ICON_NAME                       "icon-name"
#define GLADE_TAG_IMPORTANT                       "important"
#define GLADE_TAG_CREATE_TYPE                     "create-type"


/* search child */
GladeXmlNode *   glade_xml_search_child          (GladeXmlNode * node, const gchar *name);
GladeXmlNode *   glade_xml_search_child_required (GladeXmlNode * tree, const gchar* name);

/* content */

gchar *      glade_xml_get_content (GladeXmlNode * node_in); /* Get the content of the node */
void         glade_xml_set_content (GladeXmlNode *node_in, const gchar *content);

gboolean     glade_xml_get_value_int          (GladeXmlNode * node_in, const gchar *name, int *val);
gboolean     glade_xml_get_value_int_required (GladeXmlNode * node, const gchar *name, int *val);

gchar *      glade_xml_get_value_string          (GladeXmlNode * node, const gchar *name);
gchar *      glade_xml_get_value_string_required (GladeXmlNode * node,
					    const gchar *name,
					    const gchar *xtra_info);

gboolean glade_xml_get_boolean (GladeXmlNode * node, const gchar *name, gboolean _default);

void         glade_xml_set_value (GladeXmlNode * node_in, const gchar *name, const gchar *val);

/* Properties */ 
gchar *  glade_xml_get_property_string_required (GladeXmlNode *node_in, const gchar *name, const gchar *xtra);
gchar *  glade_xml_get_property_string (GladeXmlNode *node_in, const gchar *name);
gboolean glade_xml_get_property_boolean (GladeXmlNode *node_in, const gchar *name, gboolean _default);
gdouble  glade_xml_get_property_double (GladeXmlNode *node_in, const gchar *name, gdouble _default);
gint     glade_xml_get_property_int (GladeXmlNode *node_in, const gchar *name, gint _default);
gboolean glade_xml_get_property_version (GladeXmlNode *node_in, const gchar *name, guint16 *major, guint16 *minor);
GList   *glade_xml_get_property_targetable_versions (GladeXmlNode *node_in, const gchar *name);


void glade_xml_node_set_property_string (GladeXmlNode *node_in, const gchar *name, const gchar *string);
void glade_xml_node_set_property_boolean (GladeXmlNode *node_in, const gchar *name, gboolean value);

/* Node operations */
GladeXmlNode * glade_xml_node_new (GladeXmlContext *context, const gchar *name);
GladeXmlNode * glade_xml_node_new_comment (GladeXmlContext *context, const gchar *comment);
void           glade_xml_node_delete (GladeXmlNode *node);
GladeXmlNode * glade_xml_node_get_children (GladeXmlNode *node);
GladeXmlNode * glade_xml_node_get_parent (GladeXmlNode *node_in);
GladeXmlNode * glade_xml_node_next (GladeXmlNode *node_in);
gboolean       glade_xml_node_verify (GladeXmlNode * node_in, const gchar *name);
gboolean       glade_xml_node_verify_silent (GladeXmlNode *node_in, const gchar *name);
const gchar *  glade_xml_node_get_name (GladeXmlNode *node_in);
void           glade_xml_node_append_child (GladeXmlNode * node, GladeXmlNode * child);
void           glade_xml_node_remove (GladeXmlNode *node_in);
gboolean       glade_xml_node_is_comment (GladeXmlNode *node_in);
GladeXmlNode * glade_xml_node_next_with_comments (GladeXmlNode *node_in);
GladeXmlNode * glade_xml_node_get_children_with_comments (GladeXmlNode *node);


/* Document Operatons */
GladeXmlNode * glade_xml_doc_get_root (GladeXmlDoc *doc);
GladeXmlDoc *  glade_xml_doc_new (void);
void           glade_xml_doc_set_root (GladeXmlDoc *doc, GladeXmlNode *node);
void           glade_xml_doc_free (GladeXmlDoc *doc_in);
gint           glade_xml_doc_save (GladeXmlDoc *doc_in, const gchar *full_path);

/* Parse Context */
GladeXmlContext * glade_xml_context_new     (GladeXmlDoc *doc, const gchar *name_space);
void              glade_xml_context_destroy (GladeXmlContext *context);
void              glade_xml_context_free    (GladeXmlContext *context);
GladeXmlContext * glade_xml_context_new_from_path (const gchar *full_path,
						   const gchar *nspace,
						   const gchar *root_name);
GladeXmlDoc *     glade_xml_context_get_doc (GladeXmlContext *context);

/* Dumps an xml string from a context */
gchar * glade_xml_dump_from_context (GladeXmlContext *context);

gboolean        glade_xml_load_sym_from_node (GladeXmlNode     *node_in,
					      GModule          *module,
					      gchar            *tagname,
					      gpointer         *sym_location);

G_END_DECLS

#endif /* __GLADE_XML_UTILS_H__ */
